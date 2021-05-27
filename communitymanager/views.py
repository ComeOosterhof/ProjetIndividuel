from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from communitymanager.forms import PostForm, CommentaireForm
from communitymanager.models import Communaute, Post, Commentaire


# Cette vue correspond à l'affichage de toutes les communautés
@login_required
def communautes(request):

    communautes = Communaute.objects.all()
    current_user = request.user

    # Pour clarifier l'affichage et éviter de mettre trop de code impératif dans le template,
    # ... j'ai choisi de séparer dans la vue les communautés auxquelles l'utilisateur est déjà abonné et les autres
    current_communities = []
    other_communities = []
    for communaute in communautes:
        if current_user in communaute.abonnes.all():
            current_communities.append(communaute)
        else:
            other_communities.append(communaute)

    return render(request, 'communitymanager/communautes.html', locals())


# Cette vue correspond à l'affichage du détail d'une communauté, après avoir cliqué sur son nom
@login_required
def communaute(request, id):

    communaute = get_object_or_404(Communaute, id=id)
    posts = Post.objects.filter(communaute=communaute)

    return render(request, 'communitymanager/communaute.html', locals())


# Cette vue correspond à l'affichage du détail d'un post, après avoir cliqué sur son nom
@login_required
def post(request, id):

    post = get_object_or_404(Post, id=id)
    commentaires = Commentaire.objects.filter(post=post)

    utilisateur = request.user
    auteur = post.auteur

    return render(request, 'communitymanager/post.html', locals())


# Cette vue correspond au formulaire de création d'un post
@login_required
def nouveau_post(request, id):

    form = PostForm(request.POST or None)

    # J'ai fait le choix de conception qu'un utilisateur ne puisse créer un post que depuis ... la page d'une
    # communauté. C'est pourquoi les champs communauté et auteur ne doivent pas être remplis par l'utilisateur lui-même
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

        # Après la création d'un nouveau post, l'utilisateur est redirigé vers le détail de ce post
        return redirect('post', post.id)

    return render(request, 'communitymanager/nouveau_post.html', locals())


# Cette vue correspond au formulaire de modification d'un post
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


# Cette vue correspond au formulaire de création d'un commentaire
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


# Cette vue correspond au lien permettant de s'abonner à une communauté
@login_required
def abonnement(request, id):

    communaute = get_object_or_404(Communaute, id=id)
    communaute.abonnes.add(request.user)
    communaute.save()

    return render(request, 'communitymanager/abonnement.html', locals())


# Cette vue correspond au lien permettant de se desabonner à une communauté
@login_required
def desabonnement(request, id):

    communaute = get_object_or_404(Communaute, id=id)
    communaute.abonnes.remove(request.user)
    communaute.save()

    return render(request, 'communitymanager/desabonnement.html', locals())


# J'ai ajouté une fonctionnalité qui n'était pas demandé : la possibilité de modifier un commentaire
@login_required
def modif_commentaire(request, id):

    commentaire = get_object_or_404(Commentaire, id=id)
    post = commentaire.post

    if request.method == 'POST':
        form = CommentaireForm(request.POST, instance=commentaire)
        if form.is_valid():
            form.save()
            return redirect('post', post.id)
    else:
        form = CommentaireForm(instance=commentaire)

    return render(request, 'communitymanager/modif_commentaire.html', locals())


# Cette vue correspond au fil d'actualité
@login_required
def news_feed(request):

    utilisateur = request.user

    # On récupère d'aord les communautés auxquels l'utilisateur est abonné puis les posts de ces communautés
    communautes = Communaute.objects.filter(abonnes=utilisateur)
    posts = Post.objects.filter(communaute__in=communautes).order_by('date_creation').reverse()

    return render(request, 'communitymanager/news_feed.html', locals())
