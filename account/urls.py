from django.urls import path
from account.views import RegistrationView, LogOut, LogIn, ChangePassword


urlpatterns = [
    path("registration/", RegistrationView.as_view(), name="register"),
    path("logout/", LogOut, name="logout"),
    path("login/", LogIn.as_view(), name="login"),
    path("change-password/", ChangePassword, name="changepassword"),
]