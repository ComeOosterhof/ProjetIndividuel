from django import forms
from .models import Post, Commentaire


# Le formulaire créé à partir du modèle Post, qui permet la création ou la modification d'un post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titre', 'priorite', 'description', 'evenementiel', 'date_creation', 'date_evenement']


# Le formulaire créé à partir du modèle Commentaire, qui permet la création ou la modification d'un commentaire
class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['contenu']
