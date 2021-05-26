from django import forms
from .models import Post, Commentaire


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titre', 'priorite', 'description', 'evenementiel', 'date_creation', 'date_evenement']


class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['contenu']
