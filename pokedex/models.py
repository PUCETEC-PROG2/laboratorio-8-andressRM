from django.db import models
class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    weight = models.FloatField()
    height = models.FloatField()

    def __str__(self):
        return self.name





# Create your models here.
