from django.shortcuts import render
import requests
# Create your views here.

def index(request):
    out={}
    if request.method=="GET":
        params={"filter[text]":request.GET.get('search',"")}

        res=requests.get("https://kitsu.io/api/edge/anime/",params=params)
        # print(res.url)
        res=res.json()['data']
    return render(request,"anime/anime_home.html",context={"response":res})


def anime_episodes_view(request):
    if request.method=="POST":
        url=request.POST.get('url',False)
        if url:
            params={'page[limit]':'20','page[offset]':'0'}
            res=requests.get(url,params=params)
            if res:
                res=res.json()['data']
    return render(request,"anime/anime_episodes.html",context={"response":res})