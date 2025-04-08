from django.contrib import admin
from .models import Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'reference', 'category', 'price', 'stock_quantity', 'status', 'is_active')
    list_filter = ('category', 'status', 'is_active', 'brand', 'supplier')
    search_fields = ('name', 'reference', 'barcode', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('price', 'stock_quantity', 'is_active')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [ProductImageInline]
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'reference', 'barcode', 'description')
        }),
        ('Catégorisation', {
            'fields': ('category', 'brand', 'supplier')
        }),
        ('Prix et stock', {
            'fields': ('price', 'cost_price', 'stock_quantity', 'low_stock_threshold', 'status')
        }),
        ('Caractéristiques', {
            'fields': ('weight', 'dimensions', 'image', 'is_active')
        }),
        ('Informations supplémentaires', {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at'),
        }),
    )


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'alt_text', 'is_primary', 'created_at')
    list_filter = ('is_primary',)
    search_fields = ('product__name', 'alt_text')
    list_editable = ('is_primary',)
