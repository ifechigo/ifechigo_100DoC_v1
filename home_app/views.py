from . import models
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'base.html')


def login(request):
    return render(request, 'home_app/login.html')


def signup(request):
    return render(request, 'home_app/signup.html')


def about(request):
    return render(request, 'about.html')
