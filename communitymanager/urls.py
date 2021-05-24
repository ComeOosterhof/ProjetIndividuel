from django.urls import path
from . import views

urlpatterns = [
    path('communautes', views.communautes, name='communautes'),
    path('communaute/<id>', views.communaute, name='communaute'),
    path('post/<id>', views.post, name='post')
]
