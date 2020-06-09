from . import models
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'base.html')


def login(request):
    loginUsername = request.POST.get('loginUsername')
    loginPassword = request.POST.get('loginPassword')
    # b = models.Login.objects.create(loginPassword=loginPassword)
    # models.Login.objects.create(loginUsername=loginUsername)
    print(loginUsername, loginPassword)

    return render(request, 'home_app/login.html')


def signup(request):
    signupUsername = request.POST.get('signupUsername')
    signupEmail = request.POST.get('signupEmail')
    signupPassword = request.POST.get('signupPassword')
    signupConfirmPassword = request.POST.get('signupConfirmPassword')

    confirmation = request.POST.get
    def confirmation(signupPassword, signupConfirmPassword, result):
        if signupPassword != signupConfirmPassword:
            return 'password doesnt confirm with each other'


    print(signupUsername, signupEmail,
          signupPassword, signupConfirmPassword)

    return render(request, 'home_app/signup.html')


def about(request):
    return render(request, 'home_app/about.html')
