from django.urls import path
from .views import addMusic, homePage, musicList

app_name = 'musics'

urlpatterns = [
    path('', homePage, name='home_page'), 
    path('add/', addMusic, name='add_music'), 
    path('list/', musicList, name='music_list'),  # Adding the musicList URL pattern
]
