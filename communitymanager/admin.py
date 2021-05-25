from django.contrib import admin
from .models import Communaute, Post, Priorite, Commentaire

# Register your models here.

admin.site.register(Communaute)
admin.site.register(Post)
admin.site.register(Priorite)
admin.site.register(Commentaire)
