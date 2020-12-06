from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.dash,name="dash"),
    path('profile',views.profile,name="profile")
]
