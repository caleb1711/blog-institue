from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from accounts.forms import SignUpForm  

User = get_user_model()

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
