# produits/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Page d'accueil
    path('inscription/', views.inscription, name='inscription'),  # Page d'inscription
    path('connexion/', views.connexion, name='connexion'),  # Page de connexion
    path('deconnexion/', views.deconnexion, name='deconnexion'),  # Déconnexion
    path('liste/', views.liste_produits, name='liste_produits'),  # Liste des produits
]
