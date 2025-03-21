# produits/models.py
from django.db import models

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.nom
