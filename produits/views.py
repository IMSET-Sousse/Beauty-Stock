# produits/views.py

from django.shortcuts import render
from .models import Produit

def home(request):
    # Affiche une page d'accueil simple
    return render(request, 'produits/home.html')

def liste_produits(request):
    # Affiche la liste des produits
    produits = Produit.objects.all()
    return render(request, 'produits/liste_produits.html', {'produits': produits})
