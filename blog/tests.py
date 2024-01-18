from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.test import RequestFactory
from django.contrib.auth import get_user_model
from blog.views import HomeView
from blog.models import Blog

User = get_user_model()

# Home View Test
class HomeViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='abu@gmail.com', password='testpassword')

        image1 = SimpleUploadedFile("image1.jpg", b"file_content", content_type="image/jpeg")
        image2 = SimpleUploadedFile("image2.jpg", b"file_content", content_type="image/jpeg")

        self.blog1 = Blog.objects.create(user=self.user, title="Blog 1", content="Content 1", image=image1)
        self.blog2 = Blog.objects.create(user=self.user, title="Blog 2", content="Content 2", image=image2)


        self.factory = RequestFactory()

    def test_home_view(self):
        self.client.login(email='abu@gmail.com', password='testpassword')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'index.html')


# My Blogs Test Cases 
class MyBlogsViewTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(email='abu@gmail.com', password='testpassword')
        self.factory = RequestFactory()

    def test_my_blogs_view_authenticated(self):
        self.client.login(email='abu@gmail.com', password='testpassword')

        image1 = SimpleUploadedFile("image1.jpg", b"file_content", content_type="image/jpeg")

        Blog.objects.create(title='Test Blog', content='Test Content', user=self.user, image=image1)

        response = self.client.get(reverse('myblogs'))

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'blog/myblogs.html')

        self.assertIn('blogs', response.context)
        self.assertEqual(len(response.context['blogs']), 1)

    def test_my_blogs_view_unauthenticated(self):
        response = self.client.get(reverse('myblogs'))
        self.assertRedirects(response, '/accounts/login/?next=' + reverse('myblogs'))

# Delete Blog View Test Case

class DeleteBlogViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='abu@gmail.com', password='testpassword')
        
        image1 = SimpleUploadedFile("image1.jpg", b"file_content", content_type="image/jpeg")
        self.blog = Blog.objects.create(title='Test Blog', content='Test Content', user=self.user, image=image1)

    def test_delete_blog_authenticated_user(self):
        self.client.login(email='abu@gmail.com', password='testpassword')

        initial_count = Blog.objects.count()

        response = self.client.post(reverse('deleteblog', args=[self.blog.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Blog.objects.count(), initial_count - 1)
        self.assertRedirects(response, reverse('myblogs'))