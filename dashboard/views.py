from django.shortcuts import render
from products.models import Product
from stock.models import Stock
from datetime import date

def dashboard_home(request):
    total_products = Product.objects.count()
    low_stock = Stock.objects.filter(quantity__lte=10).count()
    expired_products = Product.objects.filter(expiration_date__lt=date.today()).count()

    context = {
        'total_products': total_products,
        'low_stock': low_stock,
        'expired_products': expired_products,
    }

    return render(request, 'dashboard/index.html', context)
