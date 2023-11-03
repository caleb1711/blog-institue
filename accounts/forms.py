from django import forms
from django.contrib.auth import authenticate, get_user_model, login
import threading
import uuid
from .emails import send_email
User = get_user_model()


class BaseForm(forms.Form):
    def __init__(self, request, *args, **kwargs):
        self.request = request
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class LoginForm(BaseForm):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        user = authenticate(self.request, email=email, password=password)
        if user is None:
            raise forms.ValidationError('Invalid email or password')
        cleaned_data['user'] = user
        return cleaned_data


class SignUpForm(BaseForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput)

    

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('Password must be at least 8 characters')
        return password

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('Passwords do not match')
        return password2

    def save(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        password = self.cleaned_data.get('password')
        email = self.cleaned_data.get('email')
        user = User.objects.create_user(email=email, password=password, first_name=first_name)
        login(self.request, user)
        return user
    

class ForgotForm(BaseForm):
    email = forms.EmailField()
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError('No account found with this email')
        user = User.objects.get(email=email)
        token = uuid.uuid4()
        user.forgot_email_token = token
        user.save()
        host = self.request.get_host()
        url = f"/{host}/accounts/reset/{token}/"
        subject = "Reset Password"
        text_content = f"Hi {user.first_name}! you reset password link is {url}"
        recipient_list = [email]
        thread = threading.Thread(target=send_email, args = (subject, text_content, recipient_list, False))
        thread.start()
        return email
    


class ResetForm(BaseForm):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput)
    token = forms.CharField(widget=forms.HiddenInput)

    def clean_token(self):
        token = self.cleaned_data.get('token')
        if not User.objects.filter(forgot_email_token=token).exists():
            raise forms.ValidationError('Token is expired') 
        return token
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('Password must be at least 8 characters')
        return password

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('Passwords do not match')
        return password2

    def save(self):
        password = self.cleaned_data.get('password')
        token = self.cleaned_data.get('token')
        user = User.objects.get(forgot_email_token=token)
        user.set_password(password)
        user.save()
        return user