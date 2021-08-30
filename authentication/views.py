from django.shortcuts import render
from django.core.checks import messages
from django.db import models
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def dashboard(request):
    return render(request, "registration/dashboard.html")

# def homepage(request):
#     # print(request.user)
    # if request.user.is_anonymous:
    #     return redirect('/login')
    # return render(request, 'registration/homepage.html')

def mediaLogin(request):
    if request.user.is_anonymous:
        return render(request, "registration/login.html")
    return render(request, 'registration/homepage.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'registration/login.html')
    return render(request, 'registration/login.html')
    

def logoutUser(request):
    logout(request)
    return redirect('/login')

