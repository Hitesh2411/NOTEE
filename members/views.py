from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError


class LoginView(TemplateView):
    template_name = 'members/login.html'
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('notesList:notes')
        else:
            messages.success(request,("Enter Valid Credentials"))
            return render(request, 'members/login.html', {})


class RegisterView(TemplateView):
    template_name = 'members/register.html'
    
    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confpassword = request.POST.get('confpassword')
        
        if password != confpassword:
            messages.error(request, "Passwords do not match.")
            return render(request, self.template_name)

        try:
            User.objects.create_user(username=username, email=email, password=password)
            
            messages.success(request,("Registration is succesful"))
            return redirect('members:login')
        except IntegrityError:
            messages.success(request,("User already Exists"))
            return render(request, self.template_name)


def logout_view(request):
    logout(request)
    return redirect('notesList:home')