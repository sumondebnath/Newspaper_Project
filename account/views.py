from django.shortcuts import render, redirect
from account.forms import RegistrationForm
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class RegistrationView(FormView):
    template_name = "register.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        # print(user.username)
        # login(self.request, user)
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        confirm_link = f"https://newshub-orxl.onrender.com/accounts/active/{uid}/{token}"
        email_subject = "Confirm Your Email."
        email_body = render_to_string("email.html", {"confirm_link":confirm_link})
        email = EmailMultiAlternatives(email_subject, "", to=[user.email])
        email.attach_alternative(email_body, "text/html")
        email.send()
        return super().form_valid(form)
    

def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    
    except User.DoesNotExist:
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect("login")
    else:
        return redirect("register")


def LogOut(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("home")
    
class LogIn(LoginView):
    template_name = "login.html"

    def get_success_url(self):
        return reverse_lazy("home")
    

def ChangePassword(request):
    if request.method == "POST":
        form = SetPasswordForm(user=request.user, data= request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("home")
    else:
        form = SetPasswordForm(user = request.user)
    return render(request, "password.html", {"form":form})