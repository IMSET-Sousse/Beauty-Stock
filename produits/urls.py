# produits/urls.py

from django.urls import path
from . import views  # Assure-toi que tu importes les vues

urlpatterns = [
    path('', views.home, name='home'),  # Page d'accueil
    path('produits/', views.liste_produits, name='liste_produits'),  # Liste des produits
]
