from crypt import crypt
import re
from django.urls import reverse
from django.shortcuts import render,redirect
from utils import get_database
from django.contrib.auth import login
import bcrypt

# Create your views here.


def SignupView(request):
    if(request.method=="POST"):
        collection=get_database("users")
        mailid=request.POST.get("mail")
        print(collection.find_one({"mail":mailid}))
        if collection.find_one({"mail":mailid}):
           return render(request,"accounts/sign_up.html",context={"exception_message":mailid+" already exists"}) 
        salt=bcrypt.gensalt()
        hashed_password=bcrypt.hashpw(str(request.POST.get("password")).encode('utf-8'),salt)
        form_data=dict(request.POST)
        for key,value in form_data.items():
            form_data[key]=value[0]
        form_data.pop("csrfmiddlewaretoken")
        form_data['password']=hashed_password
        res=collection.insert_one(form_data)
        if res.acknowledged:
            # print("inserted")
            return redirect(reverse("accounts:login"))
        return redirect(reverse("accounts:signup"))
    return render(request,"accounts/sign_up.html")



def LoginView(request):
    if request.method=="POST":
        collection=get_database("users")
        mailid=request.POST.get("email")
        password=request.POST.get("password")
        user=collection.find_one({'mail':mailid})
        if user:    
            password=str(password).encode("UTF-8")
            hash_pwd=user['password']
            if bcrypt.checkpw(password,hash_pwd):
                # login(request)
                request.session['logged_in']=True
                print(user['name'])
                request.session['username']=user['name']
                return redirect(reverse("home"))
            else:
                return render(request,"accounts/login.html",context={"error_message":"wrong password"})
        else:
            return render(request,"accounts/login.html",context={"user_not_found":True})

    return render(request,"accounts/login.html")


def LogOutView(request):
    request.session['logged_in']=False
    return redirect(reverse("home"))