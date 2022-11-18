"""Wzoce URL dla users"""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    #domyślne wzorce URL uwierzytelnienia
    path('', include('django.contrib.auth.urls')),

    #rejestracja użytkownika
    path('register/', views.register, name='register')
]