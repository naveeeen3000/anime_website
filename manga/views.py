from django.shortcuts import render
import requests
import json
# Create your views here.


def index(request):
    out={}
    if request.method=="GET":
        res=requests.get("https://kitsu.io/api/edge/anime/?filter[text]="+request.GET.get('search',""))
        res=res.json()['data']
        # res=type(res)
        # out['attr']=res['attributes']
    return render(request,"index.html",context={"response":res})
