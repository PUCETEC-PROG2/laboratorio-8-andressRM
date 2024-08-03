from django.db import models

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    level = models.IntegerField()
    image_url = models.ImageField(upload_to='trainers/', default='')  

    def __str__(self):
        return self.name

class Pokemon(models.Model):
    TYPE_CHOICES = [
        ('Fire', 'Fire'),
        ('Water', 'Water'),
        ('Grass', 'Grass'),
        ('Electric', 'Electric'),
        ('Ice', 'Ice'),
        ('Fighting', 'Fighting'),
        ('Poison', 'Poison'),
        ('Ground', 'Ground'),
        ('Flying', 'Flying'),
        ('Psychic', 'Psychic'),
        ('Bug', 'Bug'),
        ('Rock', 'Rock'),
        ('Ghost', 'Ghost'),
        ('Dragon', 'Dragon'),
        ('Dark', 'Dark'),
        ('Steel', 'Steel'),
        ('Fairy', 'Fairy'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    height = models.FloatField()
    weight = models.FloatField()
    attack = models.CharField(max_length=100, default='Tackle')
    image_url = models.ImageField(upload_to='pokemons/', default='')
    audio_url = models.FileField(upload_to='audio/', default='', blank=True, null=True)  
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True, blank=True, related_name='pokemons')

    def __str__(self):
        return self.name