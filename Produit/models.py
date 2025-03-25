from django.db import models
from django.utils import timezone

class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_creation = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.titre