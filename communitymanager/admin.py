from django.contrib import admin
from .models import Communaute, Post, Priorite, Commentaire

# Register your models here.

# On enregistre les modèles dans l'administration pour pouvoir les manipuler
admin.site.register(Communaute)
admin.site.register(Post)
admin.site.register(Priorite)
admin.site.register(Commentaire)
