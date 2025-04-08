from django import forms
from .models import Product, ProductImage


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'reference', 'barcode', 'description', 'category',
            'price', 'cost_price', 'stock_quantity', 'low_stock_threshold',
            'brand', 'supplier', 'weight', 'dimensions', 'image', 'is_active'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'dimensions': forms.TextInput(attrs={'placeholder': 'L x l x H (cm)'}),
        }


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image', 'alt_text', 'is_primary']


ProductImageFormSet = forms.inlineformset_factory(
    Product, ProductImage, form=ProductImageForm,
    extra=3, can_delete=True, max_num=5
)
