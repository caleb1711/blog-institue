
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views import View
from django.contrib import messages
from accounts.models import User
from accounts.forms import LoginForm, SignUpForm, ForgotForm, ResetForm

# Sign Up 
class SignUpView(View):
    def post(self, request):
        form = SignUpForm(request, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for creating your account! you are successfully logged in to the system")
            return redirect('home')
        return render(request, "accounts/signup.html", {"form": form})
    
    def get(self, request):
        form = SignUpForm(request)
        return render(request, "accounts/signup.html", {"form": form})

# Login
class LoginView(View):
    def post(self, request):
        form = LoginForm(request, request.POST)
        if form.is_valid():
            login(request, form.cleaned_data["user"])
            next = 'home'
            messages.success(request, "Logged in successfully.")
            return redirect(next)
        return render(request, "accounts/signin.html", {"form": form})

    def get(self, request):
        form = LoginForm(request)
        return render(request, "accounts/signin.html", {"form": form})

# Forgot
class ForgotView(View):
    def post(self, request):
        form = ForgotForm(request, request.POST)
        if form.is_valid():
            messages.success(request, "An email with reset link is sent to your email address.")
            render(request, "accounts/forgot_password.html", {"form": form})
        return render(request, "accounts/forgot_password.html", {"form": form})

    def get(self, request):
        form = ForgotForm(request)
        return render(request, "accounts/forgot_password.html", {"form": form})

# Reset
class ResetPasswordView(View):
    def post(self, request, token):
        form = ResetForm(request, request.POST)
        if form.is_valid():
            form.save()
            next = 'login'
            messages.success(request, "Your Password is Updated Successfully!")
            return redirect(next)
        return render(request, "accounts/reset_password.html", {"form": form, "token":token})

    def get(self, request, token):
        form = ResetForm(request, initial={'token': token})
        return render(request, "accounts/reset_password.html", {"form": form, "token":token})

# Logout
def user_logout(request):
    logout(request)
    messages.success(request, "Logged Out successfully.")
    return redirect("login")



