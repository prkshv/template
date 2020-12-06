from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from homee.models import roleassign
from django.conf import settings
# Create your views here.

def home(request):
    return render(request,"home.html")

def signup(request):
    x=User.objects.all()
    # if request.user.is_authenticated:
    #     return redirect("dummy")
    if request.method=="POST":
        username=request.POST['uname']
        password=request.POST['psw']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        confirmpassword=request.POST['pswconfirm']
        profilerole=request.POST['role']
        if password==confirmpassword:
            ex="no"
            z=User.objects.all()
            for p in z:
                if p.username==username:
                    ex="yes"
            if ex=="no":
                myuser=User.objects.create(username=username)
                myuser.set_password(password)
                myuser.last_name=profilerole
                myuser.save()

                q=User.objects.get(username=username)
                sample=roleassign(userr=q,role=profilerole)
                #sample=roleassign.objects.create(userr=username,role=profilerole)
                sample.save()
                
                messages.info(request,"Signup successfull")



            else:
                messages.info(request,"You already have an account")
        else:
            messages.info(request,"invalid creadentials")
    
    return render(request,"signup.html")


def signin(request):
    if request.user.is_authenticated:
        #return redirect("dummy")
        messages.info(request,"already signed in")
    if request.method=="POST":
        username=request.POST['uname']
        password=request.POST['pwd']
        user=authenticate(username=username,password=password)
        if user is not None:
            x=roleassign.objects.all()
            for j in x:
                if j.userr==user and j.role=="maker":
                    login(request,user)
                    return redirect('/makerr')
                else:
                    login(request,user)
                    return redirect('/userr')
            # login(request,user)
            #return redirect('')
            
            messages.info(request,"login success")
        else:
            messages.info(request,"login failed")
    return render(request,"signin.html")

def signout(request):
    logout(request)
    return redirect('signin')