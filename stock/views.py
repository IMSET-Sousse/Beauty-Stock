from django.shortcuts import render
from .models import Stock, StockAlert
from products.models import Product
from django.utils import timezone

def stock_dashboard(request):
    # Get all stock entries and filter by low stock
    low_stock_items = Stock.objects.filter(quantity__lte=10)  # You can change the threshold as needed
    expired_products = Product.objects.filter(expiration_date__lt=timezone.now())  # Products that are expired
    stock_alerts = StockAlert.objects.all()

    return render(request, 'stock/stock_dashboard.html', {
        'low_stock_items': low_stock_items,
        'expired_products': expired_products,
        'stock_alerts': stock_alerts,
    })
