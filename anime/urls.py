from argparse import Namespace
from django.urls import path
from . import views

app_name="anime"

urlpatterns = [
    path("anime_search/",views.index,name='anime_home'),
    path("anime_episodes/",views.anime_episodes_view,name='anime_episodes')
]
