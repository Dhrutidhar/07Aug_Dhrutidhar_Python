from django.contrib import admin
from django.urls import path
from Insurance_App import views

urlpatterns = [
    path('',views.index),


]