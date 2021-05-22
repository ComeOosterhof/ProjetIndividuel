from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.

class Communaute(models.Model):
    nom = models.CharField(max_length=30)
    abonnes = models.ManyToManyField(User)

    def __str__(self):
        return self.nom
