from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime

# Create your views here.
from communitymanager.forms import PostForm, CommentaireForm
from communitymanager.models import Communaute, Post, Commentaire


@login_required
def communautes(request):
    communautes = Communaute.objects.all()
    current_user = request.user
    current_communities = []
    other_communities = []
    for communaute in communautes:
        if current_user in communaute.abonnes.all():
            current_communities.append(communaute)
        else:
            other_communities.append(communaute)

    return render(request, 'communitymanager/communautes.html', locals())


@login_required
def communaute(request, id):
    communaute = get_object_or_404(Communaute, id=id)
    posts = Post.objects.filter(communaute=communaute)

    return render(request, 'communitymanager/communaute.html', locals())


@login_required
def post(request, id):

    post = get_object_or_404(Post, id=id)
    commentaires = Commentaire.objects.filter(post=post)

    utilisateur = request.user
    auteur = post.auteur

    peut_modifier = False
    if utilisateur == auteur:
        peut_modifier = True

    return render(request, 'communitymanager/post.html', locals())


@login_required
def nouveau_post(request, id):
    form = PostForm(request.POST or None)

    communaute = get_object_or_404(Communaute, id=id)
    auteur = request.user

    if form.is_valid():
        titre = form.cleaned_data['titre']
        priorite = form.cleaned_data['priorite']
        description = form.cleaned_data['description']
        evenementiel = form.cleaned_data['evenementiel']
        date_creation = form.cleaned_data['date_creation']
        date_evenement = form.cleaned_data['date_evenement']

        post = form.save(commit=False)

        post.communaute = communaute
        post.auteur = auteur

        post.save()

        return redirect('post', post.id)

    return render(request, 'communitymanager/nouveau_post.html', locals())


@login_required
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


@login_required
def nouveau_commentaire(request, id):
    form = CommentaireForm(request.POST or None)

    post = get_object_or_404(Post, id=id)
    auteur = request.user

    if form.is_valid():
        contenu = form.cleaned_data['contenu']

        commentaire = form.save(commit=False)
        commentaire.auteur = auteur
        commentaire.post = post

        commentaire.save()

        return redirect('post', post.id)

    return render(request, 'communitymanager/nouveau_commentaire.html', locals())


@login_required
def abonnement(request, id):
    communaute = get_object_or_404(Communaute, id=id)
    communaute.abonnes.add(request.user)
    communaute.save()

    return render(request, 'communitymanager/abonnement.html', locals())


@login_required
def desabonnement(request, id):
    communaute = get_object_or_404(Communaute, id=id)
    communaute.abonnes.remove(request.user)
    communaute.save()

    return render(request, 'communitymanager/desabonnement.html', locals())
