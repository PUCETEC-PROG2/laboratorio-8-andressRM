# pokedex/models.py

from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    height = models.FloatField()
    weight = models.FloatField()
    attack = models.CharField(max_length=100, default='Tackle')
    image_url = models.CharField(max_length=200, default='')
    audio_url = models.CharField(max_length=200, default='')  # MP3

    def __str__(self):
        return self.name

# pokedex/models.py

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    level = models.IntegerField()
    image_url = models.ImageField(upload_to='trainers/', default='')  

    def __str__(self):
        return self.name
