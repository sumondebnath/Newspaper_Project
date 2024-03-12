from django.shortcuts import render, redirect
from account.forms import RegistrationForm, ImageForm, UpdateForm
from django.views.generic import FormView, View
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User
from account.models import UserAccount
from article.models import Article

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
        # user.is_active = False
        user.save()
        # print(user.username)
        # login(self.request, user)
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        print(token, uid)
        confirm_link = f"https://newshub-orxl.onrender.com/accounts/active/{uid}/{token}"
        email_subject = "Confirm Your Email."
        email_body = render_to_string("email.html", {"confirm_link":confirm_link})
        email = EmailMultiAlternatives(email_subject, "", to=[user.email])
        email.attach_alternative(email_body, "text/html")
        email.send()
        return super().form_valid(form)
    
class UpdateAccount(View):
    template_name = "update.html"

    def get(self, request):
        form = UpdateForm(instance=self.request.user)
        return render(request, self.template_name, {"form":form})
    
    def post(self, request):
        if request.method == "POST":
            form = UpdateForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect("profile")
        else:
            form = UpdateForm()
        return render(request, self.template_name, {"form":form})
    

def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
        print(uid ,user)
    
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


def Profile(request):
    user = request.user

    user_articles = Article.objects.filter(user=user)
    
    return render(request, "profile.html", {"user":user, "user_articles":user_articles})


def SetImage(request):
    if request.method =="POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            user_account, created = UserAccount.objects.get_or_create(user=current_user)
            user_account.image = form.cleaned_data["image"]
            user_account.save()
            return redirect("profile")
    else:
        form = ImageForm()
    return render(request, "setimage.html", {"form":form})