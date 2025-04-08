from django.db import models
from product.models import Product


class Stock(models.Model):
    product = models.ForeignKey(Product, related_name='stock', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Stock for {self.product.name}"

    # Method to check if stock is low
    def is_stock_low(self, threshold=10):
        return self.quantity <= threshold

class StockAlert(models.Model):
    product = models.ForeignKey(Product, related_name='alerts', on_delete=models.CASCADE)
    threshold = models.PositiveIntegerField(default=10)  # Alert when stock falls below this threshold

    def __str__(self):
        return f"Alert for {self.product.name} when stock is below {self.threshold}"
