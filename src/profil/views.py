from django.shortcuts import render, redirect
from .form import UserRegistrationForm
from django.contrib.auth.views import LoginView

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:home")
    else:
        form = UserRegistrationForm()
    return render(request, "profil\signup.html",{"form":form})

class login(LoginView):
    template_name = "registration/log.html"