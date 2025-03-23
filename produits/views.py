from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm
from .models import Produit
from django.contrib.auth.decorators import login_required

# Vue pour la page de connexion
def connexion(request):
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

# Vue pour la déconnexion de l'utilisateur
def deconnexion(request):
    logout(request)  # Effectue la déconnexion
    return redirect('home')  # Redirige vers la page d'accueil après la déconnexion

# Vue de la page d'accueil (uniquement une vue 'home')
@login_required
def home(request):
    return render(request, 'produits/home.html')  # Assurez-vous que ce fichier existe

# Vue pour afficher la liste des produits
@login_required
def liste_produits(request):
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
