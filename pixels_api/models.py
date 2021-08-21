from django.db import models

# Create your models here.
class Games(models.Model):
    name = models.CharField(max_length=32)
    image = models.URLField()
    genre = models.CharField(max_length=32)

class UserAccount(models.Model):
    username = models.CharField(max_length=75, unique=True)
    password = models.CharField(max_length=1000)
    image = models.URLField(blank=True)
    name = models.CharField(max_length=32,blank=True)
    age = models.CharField(max_length=32,blank=True)
    fav_console = models.CharField(max_length=32,blank=True)
    fav_games = models.ManyToManyField(Games,blank=True)
