from django.contrib import admin
from .models import (
    Blog,
    Comment
)
# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("user", "image", "title", "content", "created_at", "updated_at")
    list_filter = ("user",)  
    search_fields = ("title",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "blog","content", "created_at", "updated_at")
    list_filter = ("user",)  
    search_fields = ("content",)