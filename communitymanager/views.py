from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime

# Create your views here.
from communitymanager.forms import PostForm
from communitymanager.models import Communaute, Post, Commentaire


def communautes(request):
    communautes = Communaute.objects.all()
    current_user = request.user
    current_communities = []
    other_communities = []
    for communaute in communautes:
        if Communaute.objects.filter(id=current_user.id).exists():
            current_communities.append(communaute)
        else:
            other_communities.append(communaute)

    return render(request, 'communitymanager/communautes.html', locals())


def communaute(request, id):
    communaute = get_object_or_404(Communaute, id=id)
    posts = Post.objects.filter(communaute=communaute)

    return render(request, 'communitymanager/communaute.html', locals())


def post(request, id):
    post = get_object_or_404(Post, id=id)
    commentaires = Commentaire.objects.filter(post=post)

    return render(request, 'communitymanager/post.html', locals())


def nouveau_post(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        titre = form.cleaned_data['titre']
        priorite = form.cleaned_data['priorite']
        description = form.cleaned_data['description']
        auteur = form.cleaned_data['auteur']
        evenementiel = form.cleaned_data['evenementiel']
        date_creation = form.cleaned_data['date_creation']
        date_evenement = form.cleaned_data['date_evenement']
        communaute = form.cleaned_data['communaute']

        # envoi = True

        post = form.save(commit=True)

        return redirect('post', post.id)

    return render(request, 'communitymanager/nouveau_post.html', locals())


def modif_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post', post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'communitymanager/modif_post.html', locals())