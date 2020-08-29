from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signupPage, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('about/', views.about, name='about'),
    path('logout/', views.logoutUser, name='logout'),


    path('welcome/', views.welcome, name='welcome'),
]
