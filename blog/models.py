from django.db import models
from accounts.models import User
# Create your models here.

# Blog Model
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs", help_text=("Add the owner of blog"))
    image = models.ImageField(upload_to="blog_images/", help_text=("Add Blog image"))
    title = models.CharField(max_length=500, help_text=("Add Blog title"))
    content = models.TextField(help_text=("Add Blog content"))
    
    upvotes = models.PositiveIntegerField(default=0) 
    downvotes = models.PositiveIntegerField(default=0)    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Blog" 
        verbose_name_plural = "Blogs"

    def __str__(self) :
        return f"{self.title}" or f"Blog-{self.id}"
    
# Comment Model
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commentblogs", help_text=("Add the blog"))
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments", help_text=("Add the comment"))
    content = models.TextField(help_text=("Add Blog content"))
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Comment" 
        verbose_name_plural = "Comments"

    def __str__(self) :
        return f"{self.content}" or f"Comment-{self.id}"