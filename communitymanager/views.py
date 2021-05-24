from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from datetime import datetime

# Create your views here.
from communitymanager.models import Communaute, Post


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
