# Cahier des Charges - Application de gestion de produits cosmétiques "Beauty_Stock"

## 1. Présentation du Projet
### 1.1 Contexte

**Beauty_Stock** est une application web permettant aux administrateurs de gérer les produits cosmétiques d'une boutique en ligne. Cette plateforme permet d’ajouter, modifier, supprimer et afficher des produits cosmétiques avec des informations détaillées. Elle vise à fournir une gestion optimisée pour les stocks et une interface simple d’utilisation.

### 1.2 Objectifs
- Offrir une **interface intuitive** pour gérer les produits cosmétiques. 
- Permettre l’ajout, la modification et la suppression de **produits** avec des informations complètes (nom, description, catégorie, prix, ingrédients, quantité en stock, date de péremption).
- Intégrer **une gestion dynamique** des stocks et des alertes en cas de faible quantité. 
- Mettre en place **un système de filtrage** et de recherche efficace pour les produits. 
- Assurer **une interface responsive et accessible**, compatible avec tous les appareils (desktop et mobile).

## 2. Structure et Pages de l'Application
### 2.1 Pages Principales (Accès Public)
#### 1. Accueil
- Présentation de la plateforme et des principales catégories de produits cosmétiques (soins de la peau, maquillage, cheveux, etc.). 
- Affichage des produits populaires et des promotions.

#### 2. Page de Recherche
- Champ de recherche pour trouver des produits par nom, catégorie ou prix. 
- Filtres de recherche : catégorie, prix, date de péremption, etc.

#### 3. Page de Détail d'un Produit 
- Informations complètes sur le produit : nom, description, catégorie, prix, ingrédients, quantité en stock, date de péremption. 
- Option d’ajout au panier.

### 2.2 Pages Utilisateurs (Connexion Requise)

#### 4. Inscription & Connexion

- Formulaire d’inscription avec possibilité de se connecter via email ou réseaux sociaux. 
- Authentification sécurisée.

#### 5. Tableau de Bord Utilisateur (Admin)
- Vue d’ensemble des produits en stock. 
- Gestion des produits : ajout, modification, suppression.
 - Visualisation des produits à faible stock ou expirés.

 #### 6. Gestion des Produits 
 - Formulaires pour ajouter/modifier un produit : champ pour le nom, la description, la catégorie, le prix, les ingrédients, la quantité en stock, la date de péremption. 
 - Affichage des produits avec possibilité de filtrer selon différents critères (par exemple, par catégorie, prix, etc.).

 #### 7. Page de Statistiques

 - Statistiques des produits populaires, des produits en rupture de stock et des ventes.

 ### 2.3 Pages Administratives

 #### 8. Dashboard Admin 

 - Vue d’ensemble des produits. 
 - Gestion des utilisateurs (administrateurs et clients). 
 - Gestion des commandes.

 #### 9. Gestion des Catégories

 - Création, modification et suppression des catégories de produits (soins de la peau, maquillage, cheveux, etc.).

 ### 2.4 Pages d'Alertes et Notifications

 #### 10. Alertes de Stock Faible 

 - Notifications envoyées à l’administrateur lorsque la quantité en stock d’un produit atteint un seuil critique.

 ## 3. Architecture Technique 
### 3.1  Stack Technologique
- **Frontend** : HTML, CSS (Bootstrap ou TailwindCSS pour le responsive design), JavaScript .

- **Backend** : Django pour la gestion des données et des fonctionnalités de l’application.

- **Base de données** : MySQL pour la gestion des données des produits, utilisateurs et commandes.


