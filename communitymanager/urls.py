from django.urls import path
from . import views

# Pour simplifier, j'ai donné le même nom à chaque fois au modèle d'URL et à la vue correspondante
urlpatterns = [
    path('communautes', views.communautes, name='communautes'),
    path('communaute/<id>', views.communaute, name='communaute'),
    path('post/<id>', views.post, name='post'),
    path('nouveau_post/<id>', views.nouveau_post, name='nouveau_post'),
    path('modif_post/<id>', views.modif_post, name='modif_post'),
    path('nouveau_commentaire/<id>', views.nouveau_commentaire, name='nouveau_commentaire'),
    path('abonnement/<id>', views.abonnement, name='abonnement'),
    path('desabonnement/<id>', views.desabonnement, name='desabonnement'),
    path('modif_commentaire/<id>', views.modif_commentaire, name='modif_commentaire'),
    path('news_feed', views.news_feed, name='news_feed')
]
