from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Accueil (uniquement pour les utilisateurs connectés)
    path('produits/', views.liste_produits, name='liste_produits'),  # Liste des produits
    path('inscription/', views.inscription, name='inscription'),  # Formulaire d'inscription
    path('connexion/', views.connexion, name='connexion'),  # Formulaire de connexion
    path('deconnexion/', views.deconnexion, name='deconnexion'),  # Déconnexion
]
