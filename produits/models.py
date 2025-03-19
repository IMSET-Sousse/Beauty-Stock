# produits/models.py

from django.db import models

class Produit(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    categorie = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    ingredients = models.TextField()
    quantite_stock = models.IntegerField()
    date_peremption = models.DateField()

    def __str__(self):
        return self.nom
