from django.db import models
from django import forms

# Create your models here.
class song(models.Model):
    song_slug = models.AutoField(primary_key=True, unique=True)
    name = models.TextField(max_length=50)
    desc = models.TextField(max_length=150)
    cover_album = models.ImageField()
    audio_file = models.FileField(blank=True, null=True)
    artist_name = models.TextField(max_length=20, default="artist unknown")

    def __str__(self):
        return self.name
