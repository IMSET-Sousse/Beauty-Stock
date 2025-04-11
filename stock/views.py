# stock/views.py

from django.shortcuts import render , redirect
from .models import Products

def dashboard(request):
    products = Products.objects.all()
    return render(request, 'stock/dashboard.html', {'products': products})

def home(request):
    return render(request, 'stock/home.html')

def add_product(request):
    return render(request, 'stock/add_product.html')

def stock_entry(request):
    return render(request, 'stock/entry.html') 


def stock_exit(request):
    return render(request, 'stock/exit.html') 