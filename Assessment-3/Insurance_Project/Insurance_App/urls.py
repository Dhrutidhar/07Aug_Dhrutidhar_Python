from django.contrib import admin
from django.urls import path
from Insurance_App import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('news/',views.news),
    path('service/',views.service),

]