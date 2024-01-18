from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.test import RequestFactory
from django.contrib.auth import get_user_model
from blog.views import HomeView
from blog.models import Blog, Comment
from blog.forms import AddBlogForm, EditBlogForm, BlogDetailForm

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

# Add Blog Test Case
class AddBlogViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='abu@gmail.com', password='testpassword')
        self.client.login(email='abu@gmail.com', password='testpassword')

    def test_get_add_blog(self):
        response = self.client.get(reverse('addblog'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/addblog.html')
        self.assertIsInstance(response.context['form'], AddBlogForm)

    def test_post_add_blog(self):
        initial_blog_count = Blog.objects.count()

        image = SimpleUploadedFile("image1.jpg", b"file_content", content_type="image/jpeg")
        
        post_data = {
            'image': image,
            'title': 'Test Blog',
            'content': 'Test Content',
        }
        response = self.client.post(reverse('addblog'), data=post_data, follow=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/addblog.html')


# Edit Blog test case

class EditBlogViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='abu@gmail.com', password='testpassword')
        self.client.login(email='abu@gmail.com', password='testpassword')

        image = SimpleUploadedFile("image1.jpg", b"file_content", content_type="image/jpeg")
        self.blog = Blog.objects.create(title='Test Blog', content='Test Content', user=self.user, image=image)

    def test_get_edit_blog_view(self):
        response = self.client.get(reverse('editblog', args=[self.blog.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/editblog.html')
        self.assertIsInstance(response.context['form'], EditBlogForm)

    def test_post_edit_blog_view(self):
        initial_title = self.blog.title
        initial_content = self.blog.content

        post_data = {
            'title': 'Updated Title',
            'content': 'Updated Content',
        }

        response = self.client.post(reverse('editblog', args=[self.blog.id]), data=post_data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/myblogs.html')
        self.assertContains(response, 'Your blog edited successfully!')

        updated_blog = Blog.objects.get(id=self.blog.id)

        self.assertNotEqual(updated_blog.title, initial_title)
        self.assertNotEqual(updated_blog.content, initial_content)
        self.assertEqual(updated_blog.title, 'Updated Title')
        self.assertEqual(updated_blog.content, 'Updated Content')

# Blog Details Test Case
class BlogDetailViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='abu@gmail.com', password='testpassword')
        self.client.login(email='abu@gmail.com', password='testpassword')

        image = SimpleUploadedFile("test_image.jpg", content=b"test_image_content", content_type="image/jpeg")
        self.blog = Blog.objects.create(title='Test Blog', content='Test Content', user=self.user, image=image)

    def test_get_blog_detail_view(self):
        response = self.client.get(reverse('blog_detail', args=[self.blog.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogdetails.html')
        self.assertIsInstance(response.context['form'], BlogDetailForm)
        self.assertEqual(response.context['blog'], self.blog)

    def test_post_blog_detail_view(self):
        post_data = {
            'content': 'Test Comment',
        }

        response = self.client.post(reverse('blog_detail', args=[self.blog.id]), data=post_data, follow=True)

        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, 'blogdetails.html')

        self.assertEqual(Comment.objects.count(), 1)
        saved_comment = Comment.objects.first()
        self.assertEqual(saved_comment.content, 'Test Comment')
        self.assertEqual(saved_comment.user, self.user)
        self.assertEqual(saved_comment.blog, self.blog)


# About Us View Test Case
class AboutUsViewTestCase(TestCase):
    def test_about_us_view(self):
        response = self.client.get(reverse('about'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
        self.assertContains(response, 'About Us') 


# About Us View Test Case
class DisclaimerViewTestCase(TestCase):
    def test_disclaimer_us_view(self):
        response = self.client.get(reverse('disclaimer'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'disclaimer.html')
        self.assertContains(response, 'Disclaimer') 