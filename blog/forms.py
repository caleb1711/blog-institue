from django import forms
from django.contrib.auth import  get_user_model
from .models import Blog, Comment
User = get_user_model()

# Blog Form
class AddBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['image','title', 'content']

# Comment Form 
class EditBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['image','title', 'content']

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image:
            return self.instance.image
        return image


class BlogDetailForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']