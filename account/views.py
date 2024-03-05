from django.shortcuts import render, redirect
from account.forms import RegistrationForm
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.forms import SetPasswordForm

# Create your views here.

class RegistrationView(FormView):
    template_name = "register.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.save()
        print(user)
        login(self.request, user)
        return super().form_valid(form)
    

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