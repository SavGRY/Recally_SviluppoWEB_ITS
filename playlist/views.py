from dataclasses import field
from django.shortcuts import render, redirect
from datetime import datetime
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from . import forms
from .models import Playlist, Canzone

def index(request):
    return render(request, 'playlist/home.html')

def p_list(request):
    return render(request, 'playlist/playlist_list.html')

# PLAYLIST #
class PlaylistCreateNew(LoginRequiredMixin, generic.CreateView):
    model = Playlist
    template_name = "playlist/playlist_create.html"
    form_class = forms.PlaylistForm
    success_url = reverse_lazy("playlist:playlist_list")
    
    def form_valid(self, form):
        form.instance.Owner = self.request.user
        return super().form_valid(form)

class PlaylistView(LoginRequiredMixin, generic.ListView):
    model = Playlist
    template_name = "playlist/playlist_list.html"
    
class PlaylistDetail(LoginRequiredMixin, generic.DetailView):
    model = Playlist
    template_name =  "playlist/playlist_detail.html"
    
class PlaylistDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Playlist
    template_name = "playlist/playlist_delete.html"
    success_url = reverse_lazy("playlist:playlist_list")
    
class PlaylistUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Playlist
    template_name = "playlist/playlist_update.html"
    form_class = forms.PlaylistForm
    success_url = reverse_lazy("playlist:playlist_list")

# CANZONE #
class CanzoneCreateNew(LoginRequiredMixin, generic.CreateView):
    model = Canzone
    template_name = "playlist/song_create.html"
    form_class = forms.CanzoneForm
    
    def get_success_url(self):
        return reverse("playlist:song_list", kwargs={"pk":self.object.Playlist.id})
    
    def form_valid(self, form):
        form.instance.Playlist = Playlist.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

class CanzoneView(LoginRequiredMixin, generic.ListView):
    model = Canzone
    template_name = "playlist/song_list.html"
    
    def get_queryset(self):
        return Canzone.objects.filter(Playlist=self.kwargs['pk'])
    
class CanzoneDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Canzone
    template_name = "playlist/song_delete.html"
    
    def get_success_url(self):
        return reverse("playlist:song_list", kwargs={"pk":self.object.Playlist.id})
    
class CanzoneUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Canzone
    template_name = "playlist/song_update.html"
    form_class = forms.CanzoneForm
    
    def get_success_url(self):
        return reverse("playlist:song_list", kwargs={"pk":self.object.Playlist.id})


