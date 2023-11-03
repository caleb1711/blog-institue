from django.urls import path
from .views import *

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("forgot/", ForgotView.as_view(), name="forgot"),
    path("reset/<str:token>/", ResetPasswordView.as_view(), name="reset"),
    path("logout/", user_logout, name="logout"),
]