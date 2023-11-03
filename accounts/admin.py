from django.contrib import admin
from .models import(
    User
)
from django.contrib.auth.admin  import UserAdmin

# from django.contrib.auth.models import User
# User Admin
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("email", "first_name", "last_name",  "is_staff", "is_active")
    list_filter = ("email", "is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("email", "password", "first_name", "last_name")}),
        ("Permissions", {"fields": ("is_staff", "is_active",)}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "first_name", "last_name", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)

admin.site.register(User, CustomUserAdmin)
