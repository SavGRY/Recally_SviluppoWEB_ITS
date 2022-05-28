import datetime
from django import forms
from .models import Playlist, Canzone
from django.forms.widgets import DateInput



class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = "__all__"
        widgets = {
            'AnnoCreazione': DateInput(attrs={'type':'date'})
        }
        exclude = ["Owner"]
        
class CanzoneForm(forms.ModelForm):
    class Meta:
        model = Canzone
        fields = "__all__"
        widgets = {
            'AnnoUscita': DateInput(attrs={'type':'date'})
        }
        exclude = ["Playlist"]
