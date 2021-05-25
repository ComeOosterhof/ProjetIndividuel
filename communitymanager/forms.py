from django import forms
from .models import Post, Commentaire


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['contenu']
