from django.shortcuts import render,redirect
from .forms import *
from .models import *
# Create your views here.

status=False
# def index(request):
#     global status
#     if request.method=='POST':
#         if request.POST.get('signup')=='signup':
#             newuser=signupForm(request.POST)
#             if newuser.is_valid():
#                 newuser.save()
#                 print("Signup Successfully!")
#             else:
#                 print(newuser.errors)
#         elif request.POST.get('login')=='login':

#             unm=request.POST['username']
#             pas=request.POST['password']

#             user=signupmaster.objects.filter(username=unm,password=pas)
#             uid=signupmaster.objects.get(username=unm)
#             print("UserID:",uid.id)
#             if user:
#                 print("Login Successfully!")
#                 request.session['user']=unm
#                 request.session['uid']=uid.id
#                 #msg="Login Successfully!"
#                 status=True
#                 return redirect('notes')
#             else:
#                 print("Error!Login Fail...Try again")
#     return render(request,'index.html')

def index(request):
    msg=""
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            username=newuser.cleaned_data.get('username')
            try:
                usersignup.objects.get(username=username)
                print("Username is already exists!")
                msg="Username is already exists!"
            except usersignup.DoesNotExist:
                newuser.save()
                print("Signup Successfully!")
                msg="Signup Successfully!"
        else:
            print(newuser.errors)
            msg="Something went wrong...Try again!"
    return render(request,'index.html',{'msg':msg})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def news(request):
    return render(request, 'news.html')

def service(request):
    return render(request, 'service.html')