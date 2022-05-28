from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Playlist(models.Model):
    Nome = models.CharField(max_length=20)
    AnnoCreazione = models.DateTimeField(null=True, verbose_name="Data di Creazione")
    Note = models.CharField(max_length=30, blank=True, null=True)
    Owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlist')
    
    
    def __str__(self):
        return f"Nome: {self.Nome} Created by: {self.Owner} Anno Creazione: {self.AnnoCreazione.strftime('%Y')} Note: {self.Note}"
    
    def anno(self):
        return self.AnnoCreazione.strftime("%d-%m-%Y")
    
    def nome(self):
        return f"{self.Nome}"

class Canzone(models.Model):
    Autore = models.CharField(max_length=50)
    Titolo = models.CharField(max_length=50)
    Genere = models.CharField(max_length=25)
    AnnoUscita = models.DateTimeField(null=False, verbose_name="Data di Uscita")
    Note = models.CharField(max_length=150, blank=True, null=True)
    Playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Canzoni' 
    
    def __str__(self):
        return f"Autore: {self.Autore} Titolo: {self.Titolo} Genere: {self.Genere} Anno D'uscita {self.AnnoUscita.strftime('%Y')} Note: {self.Note} Playlist: {self.Playlist}"
    
    def get_anno(self):
        return self.AnnoUscita.strftime('%Y')

