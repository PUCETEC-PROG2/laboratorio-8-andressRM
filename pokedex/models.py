# pokedex/models.py

from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    height = models.FloatField()
    weight = models.FloatField()
    attack = models.CharField(max_length=100, default='Tackle')  # Define a default value
    image_url = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name
