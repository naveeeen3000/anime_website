from django.urls import reverse
from django.shortcuts import render,redirect
from utils import get_database
# import pymongo

# Create your views here.


def SignupView(request):
    if(request.method=="POST"):
        print(request.POST.get("username"))
        collection=get_database("users")
        res=collection.insert_one({"username":request.POST.get("username"),
                                "email":request.POST.get("email"),
                                "password":request.POST.get("password")
        })
        if res.acknowledged:
            print("inserted")

        return redirect(reverse("accounts:signup"))
    return render(request,"accounts/sign_up.html")



def LoginView(request):
    return render(request,"accounts/login.html")