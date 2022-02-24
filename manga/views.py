from django.shortcuts import render
import requests
import json
# Create your views here.


def index(request):
    out={}
    if request.method=="GET":
        params={"filter[text]":request.GET.get('search',"")}
        res=requests.get("https://kitsu.io/api/edge/anime/",params=params)
        print(res.url)
        res=res.json()['data']
    return render(request,"index.html",context={"response":res})
