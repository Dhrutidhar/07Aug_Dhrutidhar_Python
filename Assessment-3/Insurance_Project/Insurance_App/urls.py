from django.contrib import admin
from django.urls import path
from Insurance_App import views

urlpatterns = [
    path('',views.index, name='index'),
    path('about/',views.about),
    path('contact/',views.contact),
    path('news/',views.news),
    path('service/',views.service),
    path('otp_verify/', views.otp_verify, name='otp_verify'),
    path('policies/', views.policies, name='policies'),
    path('user_logout/', views.user_logout),
    path('grantpolicies/<int:id>', views.grantpolicy),
    path('resetpass/',views.resetpass),
    path('newpass/', views.newpass, name='newpass'),
    path('update_profile/', views.update_profile),

]