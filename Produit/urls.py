from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.liste_articles, name='liste_articles'),
]