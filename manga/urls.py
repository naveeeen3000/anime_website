from django.urls import path
from . import views

app_name="manga"

urlpatterns=[
    path("trending",views.TrendingMangaView,name='manga_home'),
]