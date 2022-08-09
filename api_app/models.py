from django.db import models

# Create your models here.

class Criature(models.Model):
    name = models.CharField(max_length=100)
    baseStats = models.CharField(max_length=200)
    height = models.IntegerField(max_length=100)
    weight = models.IntegerField(max_length=100)
    evolutions = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name
