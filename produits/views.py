# produits/views.py
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm  # Assurez-vous que le formulaire d'inscription est bien importé
from .models import Produit  # Assurez-vous que le modèle Produit est bien importé
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

# Vue pour la page d'accueil
def home(request):
    # Affiche la page d'accueil
    return render(request, 'produits/home.html')

# Vue pour afficher la liste des produits
def liste_produits(request):
    # Affiche la liste des produits
    produits = Produit.objects.all()  # Récupère tous les produits de la base de données
    return render(request, 'produits/liste_produits.html', {'produits': produits})

# Vue pour l'inscription d'un utilisateur
def inscription(request):
    # Affiche le formulaire d'inscription
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)  # Récupère les données du formulaire d'inscription
        if form.is_valid():
            form.save()  # Sauvegarde le nouvel utilisateur
            return redirect('connexion')  # Redirige vers la page de connexion après l'inscription réussie
    else:
        form = UserRegistrationForm()  # Affiche un formulaire vide si la méthode n'est pas POST

    return render(request, 'produits/inscription.html', {'form': form})

# Vue pour la déconnexion de l'utilisateur
def deconnexion(request):
    # Déconnecte l'utilisateur en cours
    logout(request)  # Effectue la déconnexion
    return redirect('home')  # Redirige vers la page d'accueil après la déconnexion

# Vue pour la connexion d'un utilisateur
def connexion(request):
    # Gère la page de connexion
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)  # Formulaire de connexion
        if form.is_valid():
            username = form.cleaned_data.get('username')  # Récupère le nom d'utilisateur
            password = form.cleaned_data.get('password')  # Récupère le mot de passe
            user = authenticate(username=username, password=password)  # Authentifie l'utilisateur
            if user is not None:
                login(request, user)  # Connecte l'utilisateur
                return redirect('home')  # Redirige vers la page d'accueil après la connexion
    else:
        form = AuthenticationForm()  # Si ce n'est pas un POST, on crée un formulaire vide

    return render(request, 'produits/connexion.html', {'form': form})  # Retourne le formulaire de connexion
