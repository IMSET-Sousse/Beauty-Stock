from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('home/', views.home, name='home'),  # 👈 Nouvelle route pour la page d’accueil
    path('add/', views.add_product, name='add_product'),
    path('entry/', views.stock_entry, name='stock_entry'),
    path('exit/', views.stock_exit, name='stock_exit'),
    path('entry/', views.stock_entry, name='stock_entry'),
]
