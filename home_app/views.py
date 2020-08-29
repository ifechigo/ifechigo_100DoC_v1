from .forms import CreateUserForm, ProductForm
from .models import Product
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request, 'home_app/home.html')


def welcome(request):
    return render(request, 'home_app/welcome.html')


def signupPage(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, user + " created successfully")
            return redirect('login')
    context = {'form': form}
    return render(request, 'home_app/signup.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('welcome')
        else:
            messages.info(request, 'username or password is incorrect')
    context = {}
    return render(request, 'home_app/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def prod(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = ProductForm()
    return render(request, 'product', {'form': form})


@login_required(login_url='login')
def showprod(request):
    products = Product.objects.all()
    return render(request, 'showprod', {'products': products})


@login_required(login_url='login')
def editprod(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'editprod', {'product': product})


@login_required(login_url='login')
def updateprod(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST, instance=product)
    if form.is_valid():
        form.save()
        return redirect('show')
    return render(request, 'editprod', {'product': product})


@login_required(login_url='login')
def deleteprod(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('show')


def about(request):
    return render(request, 'myapp/about.html')
