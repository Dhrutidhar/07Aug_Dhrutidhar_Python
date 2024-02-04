from django.shortcuts import render,redirect
from .forms import *
from .models import *
from Insurance_Project import settings
import random
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# import requests


# Create your views here.

# status=False
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

otp = random.randint(10000,99999)

def index(request):

    msg=""
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            newuser=signupForm(request.POST)
            if newuser.is_valid():
                unm=newuser.cleaned_data.get('username')
                try:
                    usersignup.objects.get(username=unm)
                    print("Username is already exists!")
                    msg="Username is already exists!"
                except usersignup.DoesNotExist:
                    newuser.save()
                    print("Signup Successfully!")
                    msg="Signup Successfully!"
            
                #Email Send for OTP
                    global otp
                    sub="Your One time password"
                    msg=f"Hello User\n\nThanks for registration!\n\nYour One time password is {otp}\n\nPlease verify with this OTP, and enjoy services.\n\nThanks & Regards!\nTOPS Tech Team\n+91 9724799469 | www.tops-int.com"
                    from_mail=settings.EMAIL_HOST_USER
                    to_mail=[request.POST['username']]
                    send_mail(subject=sub,message=msg,from_email=from_mail,recipient_list=to_mail)
                    return redirect('otp_verify')
            else:
                print(newuser.errors)
                msg="Something went wrong...Try again!"
        elif request.POST.get('login')=='login':
            c_unm = request.POST['username']
            pas = request.POST['password']
            r = request.POST['role']    

            user = usersignup.objects.filter(username = c_unm, password = pas, role = r)
            c_id = usersignup.objects.get(username = c_unm)
            print("Current Id:", c_id)
            c_role = c_id.role
            print("Role of Current User: ",c_role)

            if user:
                print("Login Success")
                msg = "Login Success"
                status = True
                request.session["user"] = c_unm
                request.session['c_role'] = c_role
                return redirect('policies')
            else:
                msg = "Invalid Credentials..."
                print(msg)

        else:
            print(newuser.errors)
            msg="Something went wrong...Try again!"
    

    return render(request,'index.html',{'msg':msg})


msg = ""
def otp_verify(request):
    global otp
    global msg
    if request.method=='POST':
        if request.POST['otp']==str(otp):
            return redirect('index')
        else:
            msg="Invalid OTP...Please try again!"
            print(msg)
    return render(request,'otp_verify.html',{'msg':msg})

def policies(request):
    # global status
    user = request.session.get('user')
    c_role = request.session.get('c_role')
    data=user_policies_new.objects.all()
     
    # c_email = request.session.get('email')
    if request.method == "POST":
        pat_app = policies_form(request.POST)
        if pat_app.is_valid():
            pat_app.save()
            print("Policy saved")
           
            
        # send mail
            sub="Thank you"
            message = f"Hello {request.POST['fullname']}! \n\nYour policy is booked.\n\nIf any Queries, plz feel free to contact us...\nRegards \nSECUREFUTURES Company PVT. LTD.\n Mo: +91 99791 31476"
            frm_mail = settings.EMAIL_HOST_USER
            to_mail=['dhrutidharkotadiya99@gmail.com', request.POST['mail']]
            send_mail(subject=sub, message=message, from_email=frm_mail, recipient_list=to_mail)
        else:
            print(pat_app.errors)
            print("Sorry Try again")
    return render(request,'policies.html', {'c_role':c_role, 'user':user, 'data':data, 'id':id})


def grantpolicy(request, id):
    policyid=user_policies_new.objects.get(id=id)
    if request.method=='POST':
        data=grant_policy(request.POST,instance=policyid)
        if data.is_valid(): #true
            data.save()
            print("Your data has been updated!")


            sub="Policy Approval"
            message = f"Hello {request.POST['fullname']}! \n\nYour policy is Approved.\n\nIf any Queries, plz feel free to contact us...\nRegards \nSECUREFUTURES Company PVT. LTD.\n Mo: +91 99791 31476"
            frm_mail = settings.EMAIL_HOST_USER
            to_mail=['dhrutidharkotadiya99@gmail.com', request.POST['mail']]
            send_mail(subject=sub, message=message, from_email=frm_mail, recipient_list=to_mail)
            return redirect('policies')
        else:
            print(data.errors)
    return render(request, 'grantpolicies.html', {'policyid':policyid})


def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        new_user = feedback_form(request.POST)
        if new_user.is_valid():
            new_user.save()
            print("Your feedback has been submitted!")

        else:
            print(new_user.errors)

        # send mail
        sub="Thank you"
        message = f"Hello {request.POST['name']}! \n\nYour Feedback is Submitted.\n\nIf any Queries, plz feel free to contact us...\nRegards \nSECUREFUTURES Company PVT. LTD.\n Mo: +91 99791 31476"
        frm_mail = settings.EMAIL_HOST_USER
        to_mail = [request.POST['mail']]
        # to_mail=['dhrutidharkotadiya99@gmail.com', request.POST['mail']]
        send_mail(subject=sub, message=message, from_email=frm_mail, recipient_list=to_mail)
    return render(request, 'contact.html')

def news(request):
    return render(request, 'news.html')

def service(request):
    return render(request, 'service.html')



def user_logout(request):
    logout(request)
    return redirect('/')

def resetpass(request):
    msg = ""
    status = False
    if request.method == "POST":
        email_f = request.POST['username']
        mob_f = request.POST['mobile']
        try:
            user = usersignup.objects.get(username=email_f, mobile=mob_f)
            uid = user.id
            print("User id:", uid)
            request.session['uid']=uid
            status=True
            print("Email and Mobile number found...")
            msg = 'Email and Mobile number found...'
            return redirect('newpass')
        except:
            print("Error! Not Found...")
            msg = "Sorry! not found plz try again"
    return render(request, 'resetpass.html', {'msg':msg, 'status':status})


def newpass(request):
    uid = request.session.get('uid')
    cuid = usersignup.objects.get(id = uid)
    if request.method == 'POST':
        new_pass = update_form(request.POST)
        if new_pass.is_valid():
            new_pass = update_form(request.POST, instance=cuid)
            new_pass.save()
            print("Password is updated")
            return redirect('/')
        else:
            print("Error!!!!")
    return render(request, 'newpass.html')