from email.policy import default
from django.db import models

# Create your models here.

class Criature(models.Model):
    id_evolution = models.IntegerField(default=0)
    evolution = models.CharField(max_length=500)
    name = models.CharField(max_length=100, unique=True)
    height = models.IntegerField(default=0, blank=True, null=True)
    weight = models.IntegerField(default=0, blank=True, null=True)
    base_stats = models.CharField(max_length=500, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name
