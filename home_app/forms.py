from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name",
                  "last_name", "password1", "password2")


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"