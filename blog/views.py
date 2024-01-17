from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from blog.models import (
    Blog,
    Comment
)
from .forms import AddBlogForm, EditBlogForm, BlogDetailForm
# Create your views here.

# Home Page
class HomeView(View):

    def get(self, request):
        blogs = Blog.objects.all()
        context = {
            "blogs":blogs,
        }        
        return render(request, "index.html", context)
    
# My Blogs
class MyBlogsView(View):

    def get(self, request):
        user = request.user
        blogs = Blog.objects.filter(user=user)

        context = {
            "blogs":blogs,
        }        
        return render(request, "blog/myblogs.html", context)
    
# Delete Blogs
def delete_blog(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect("myblogs")



# Add Blog
class AddBlog(View):
    def post(self, request):
        user = request.user
        form = AddBlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = user
            form.save()
            messages.success(request, "Your blog added successfully!")
            return redirect('addblog')
        return render(request, "blog/addblog.html", {"form": form})

    def get(self, request):
        form = AddBlogForm()
        return render(request, "blog/addblog.html", {"form": form})
    
# Edit Blog
class EditBlog(View):
    def post(self, request, id):
        user = request.user
        blog = Blog.objects.get(id=id)
        form = EditBlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.instance.user = user
            form.save()
            messages.success(request, "Your blog edited successfully!")
            return redirect('myblogs')
        return render(request, "blog/editblog.html", {"form": form})

    def get(self, request, id):
        blog = Blog.objects.get(id=id)
        form = EditBlogForm(instance=blog)
        return render(request, "blog/editblog.html", {"form": form})
    
# Blog Detail
class BlogDetail(View):
    def post(self, request, id):
        user = request.user
        blog = Blog.objects.get(id=id)
        form = BlogDetailForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = user
            form.instance.blog = blog
            form.save()
            messages.success(request, "Your comment saved successfully!")
            return redirect(f'/blog_details/{id}/')
        return render(request, "blogdetails.html", {"form": form})

    def get(self, request, id):
        blog = Blog.objects.get(id=id)
        form = BlogDetailForm()
        return render(request, "blogdetails.html", {"form": form, "blog": blog})
    
# Privacy Policy
class PrivacyView(View):

    def get(self, request):       
        return render(request, "privacy_policy.html")
        
# About Us
class AboutUsView(View):

    def get(self, request):       
        return render(request, "about.html")
    
# Contact Us
class ContactUsView(View):

    def get(self, request):       
        return render(request, "contact.html")
    
# Disclaimer
class DisclaimerView(View):

    def get(self, request):       
        return render(request, "disclaimer.html")