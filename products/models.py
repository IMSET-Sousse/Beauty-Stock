from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from categories.models import Category


class Product(models.Model):
    STATUS_CHOICES = (
        ('in_stock', 'En stock'),
        ('low_stock', 'Stock faible'),
        ('out_of_stock', 'Rupture de stock'),
    )
    
    name = models.CharField(max_length=200, verbose_name="Nom")
    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name="Slug")
    reference = models.CharField(max_length=50, unique=True, verbose_name="Référence")
    barcode = models.CharField(max_length=50, blank=True, verbose_name="Code-barres")
    description = models.TextField(blank=True, verbose_name="Description")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Catégorie")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix de vente")
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix d'achat")
    stock_quantity = models.PositiveIntegerField(default=0, verbose_name="Quantité en stock")
    low_stock_threshold = models.PositiveIntegerField(default=10, verbose_name="Seuil de stock faible")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_stock', verbose_name="Statut")
    brand = models.CharField(max_length=100, blank=True, verbose_name="Marque")
    supplier = models.CharField(max_length=100, blank=True, verbose_name="Fournisseur")
    weight = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name="Poids (g)")
    dimensions = models.CharField(max_length=100, blank=True, verbose_name="Dimensions")
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Image principale")
    is_active = models.BooleanField(default=True, verbose_name="Actif")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de modification")
    
    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            
        # Update status based on stock quantity
        if self.stock_quantity <= 0:
            self.status = 'out_of_stock'
        elif self.stock_quantity <= self.low_stock_threshold:
            self.status = 'low_stock'
        else:
            self.status = 'in_stock'
            
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('products:product_detail', kwargs={'slug': self.slug})
    
    @property
    def is_in_stock(self):
        return self.stock_quantity > 0
    
    @property
    def profit_margin(self):
        if self.cost_price > 0:
            return ((self.price - self.cost_price) / self.price) * 100
        return 0


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name="Produit")
    image = models.ImageField(upload_to='products/', verbose_name="Image")
    alt_text = models.CharField(max_length=100, blank=True, verbose_name="Texte alternatif")
    is_primary = models.BooleanField(default=False, verbose_name="Image principale")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    
    class Meta:
        verbose_name = "Image du produit"
        verbose_name_plural = "Images des produits"
        ordering = ['-is_primary', 'created_at']
    
    def __str__(self):
        return f"Image de {self.product.name}"
