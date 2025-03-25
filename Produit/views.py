from django.shortcuts import render
from .models import Article

def liste_articles(request):
    articles = Article.objects.all().order_by('-date_creation')
    return render(request, 'blog/liste_articles.html', {'articles': articles})