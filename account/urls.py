from django.urls import path
from account.views import RegistrationView, LogOut, LogIn, ChangePassword, activate


urlpatterns = [
    path("registration/", RegistrationView.as_view(), name="register"),
    path("logout/", LogOut, name="logout"),
    path("login/", LogIn.as_view(), name="login"),
    path("change-password/", ChangePassword, name="changepassword"),
    path("active/<uid64>/<token>/", activate, name="activate"),
]