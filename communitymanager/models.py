from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.

# Le modèle correspondant à une communauté
class Communaute(models.Model):
    nom = models.CharField(max_length=30)
    abonnes = models.ManyToManyField(User)

    def __str__(self):
        return self.nom


# La priorité est un attribut possible d'un post
class Priorite(models.Model):
    label = models.CharField(max_length=50)

    def __str__(self):
        return self.label


# Le modèle correspondant à un post
class Post(models.Model):
    titre = models.CharField(max_length=50, default='title')
    priorite = models.ForeignKey('Priorite', on_delete=models.CASCADE)
    description = models.CharField(max_length=140)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    evenementiel = models.BooleanField(default=False)
    date_creation = models.DateTimeField(default=timezone.now, verbose_name="Date de création")
    date_evenement = models.DateTimeField(default=timezone.now, verbose_name="Date de l'évènement")
    communaute = models.ForeignKey('Communaute', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "post"

        # On choisit d'ordonner les posts par date de création
        ordering = ['date_creation']

    def __str__(self):
        return self.titre


# Le modèle correspondant à un commentaire
class Commentaire(models.Model):
    contenu = models.TextField(null=True)
    date_creation = models.DateTimeField(default=timezone.now, verbose_name="Date de création")
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "commentaire"
        ordering = ['date_creation']

    def __str__(self):
        return self.contenu
