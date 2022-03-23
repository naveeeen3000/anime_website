from django.shortcuts import render
import requests
import json
# Create your views here.


def TrendingMangaView(request):
    out={}
    url="https://kitsu.io/api/edge/trending/manga"
    res=requests.get(url)
    if res:
        res=res.json()['data']
        return render(request,"manga/manga_home.html",context={'response':res})
    return render(request,"manga/manga_home.html")