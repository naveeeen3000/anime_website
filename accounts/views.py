from django.shortcuts import render

# Create your views here.


def SigninView(request):
    return render(request,"accounts/sign_in.html")