from django.contrib import admin
from django.urls import path, include
from . import views

app_name="playlist"

urlpatterns = [
    # PLAYLIST #
    path('home/', views.index, name="home"),
    path("create/", views.PlaylistCreateNew.as_view(), name="playlist_create"),
    path("list/", views.PlaylistView.as_view(), name="playlist_list"),
    path("playlist_detail/<pk>", views.PlaylistDetail.as_view(), name="playlist_detail"),
    path("playlist_delete/<pk>", views.PlaylistDeleteView.as_view(), name="playlist_delete"),
    path("playlist_update/<pk>", views.PlaylistUpdateView.as_view(), name="playlist_update"),
        # CANZONE #
    path("<pk>/song_create/", views.CanzoneCreateNew.as_view(), name="song_create"),
    path("<pk>/song_list/", views.CanzoneView.as_view(), name="song_list"),
    path("song_update/<pk>", views.CanzoneUpdateView.as_view(), name="song_update"),
    path("song_delete/<pk>", views.CanzoneDeleteView.as_view(), name="song_delete"),    
    
]
