from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from datetime import datetime

# Create your views here.
from communitymanager.models import Communaute


def communautes(request):
    communautes = Communaute.objects.all()
    
    return render(request, 'communautes.html', locals())
