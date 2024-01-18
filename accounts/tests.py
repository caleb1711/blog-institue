from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from accounts.forms import SignUpForm  

User = get_user_model()

# Sign Up View Test
class SignUpViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('signup')

    def test_signup_view_get(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signup.html')
        self.assertIsInstance(response.context['form'], SignUpForm)

    def test_signup_view_post_valid_data(self):
        user_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'password': 'Securepassword.123',
            'password2': 'Securepassword.123',
        }

        response = self.client.post(self.signup_url, data=user_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home')) 
        self.assertTrue(get_user_model().objects.filter(email=user_data['email']).exists())

    def test_signup_view_post_invalid_data(self):
        invalid_user_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'password': 'securepassword',
            'password2': 'securepasswordass',
        }

        response = self.client.post(self.signup_url, data=invalid_user_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signup.html')
        self.assertIsInstance(response.context['form'], SignUpForm)
        self.assertFormError(response, 'form', 'password2', 'Passwords do not match')

# Login View Test
class LoginViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="test@gmail.com", password="testpassword", first_name="test",
        )
        self.client = Client()
        self.login_url = reverse('login')  

    def test_login_view_get(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signin.html')

    def test_login_view_post_valid_data(self):
        data = {'email': 'admin@gmail.com', 'password': 'admin'}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signin.html') 

    def test_login_view_post_invalid_data(self):
        data = {'email': 'testuser@gmail.com', 'password': 'wrongpassword'}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signin.html')  
        self.assertContains(response, 'Invalid email or password') 



# Forgot Password View Test
class ForgotViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.forgot_url = reverse('forgot')

    def test_forgot_view_get(self):
        response = self.client.get(self.forgot_url)
        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, 'accounts/forgot_password.html')

    def test_forgot_view_post_valid_data(self):
        data = {'email': 'abu@gmail.com'}
        response = self.client.post(self.forgot_url, data)
        self.assertEqual(response.status_code, 200)

    def test_forgot_view_post_invalid_data(self):
        data = {'email': 'wrong...ass'}  
        response = self.client.post(self.forgot_url, data)
        self.assertEqual(response.status_code, 200)


# Reset Password View Test
class ResetPasswordViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(email="test@gmail.com", password="testpassword", first_name="test")
        self.token = default_token_generator.make_token(self.user)
        self.reset_password_url = reverse('reset', kwargs={'token': self.token})

    def test_reset_password_view_get(self):
        response = self.client.get(self.reset_password_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/reset_password.html')
        self.assertContains(response, 'value="{0}"'.format(self.token))



    def test_reset_password_view_post_invalid_data(self):
        data = {'password': 'zxcsdfsd', 'password2': 'sdfsdf'}
        response = self.client.post(self.reset_password_url, data)
        self.assertEqual(response.status_code, 200)

# Logout View Test
class UserLogoutTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@gmail.com', password='test@gmail.com')
        self.client = self.client_class()
        self.client.login(email='test@gmail.com', password='test@gmail.com')

    def test_user_logout(self):
        self.assertTrue(self.user.is_authenticated)

        response = self.client.get(reverse('logout'))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))