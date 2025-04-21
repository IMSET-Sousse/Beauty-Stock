from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Product, ProductImage
from .forms import ProductForm, ProductImageFormSet
from .models import Product

@login_required
def product_list(request):
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')
    status = request.GET.get('status', '')
    
    products = Product.objects.all()
    
    if query:
        products = products.filter(
            Q(name__icontains=query) | 
            Q(reference__icontains=query) | 
            Q(barcode__icontains=query) |
            Q(description__icontains=query)
        )
    
    if category_id:
        products = products.filter(category_id=category_id)
    
    if status:
        products = products.filter(status=status)
    
    context = {
        'products': products,
        'query': query,
        'category_id': category_id,
        'status': status,
        'title': 'Liste des produits',
    }
    
    return render(request, 'products/product_list.html', context)
@login_required
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    images = product.images.all()  # si related_name est "images"
    return render(request, 'products/product_detail.html', {
        'title': f"Détails du produit - {product.name}",
        'product': product,
        'images': images,
    })
@login_required
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    images = product.images.all()
    
    context = {
        'product': product,
        'images': images,
        'title': product.name,
    }
    
    return render(request, 'products/product_detail.html', context)


@login_required
def product_create(request):
    initial_category = request.GET.get('category', None)
    initial_data = {}
    
    if initial_category:
        initial_data['category'] = initial_category
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, initial=initial_data)
        formset = ProductImageFormSet(request.POST, request.FILES)
        
        if form.is_valid() and formset.is_valid():
            product = form.save()
            formset.instance = product
            formset.save()
            
            messages.success(request, f'Le produit "{product.name}" a été créé avec succès.')
            return redirect('products:product_detail', slug=product.slug)
    else:
        form = ProductForm(initial=initial_data)
        formset = ProductImageFormSet()
    
    context = {
        'form': form,
        'formset': formset,
        'title': 'Ajouter un produit',
    }
    
    return render(request, 'products/product_form.html', context)


@login_required
def product_update(request, slug):
    product = get_object_or_404(Product, slug=slug)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        formset = ProductImageFormSet(request.POST, request.FILES, instance=product)
        
        if form.is_valid() and formset.is_valid():
            product = form.save()
            formset.save()
            
            messages.success(request, f'Le produit "{product.name}" a été mis à jour avec succès.')
            return redirect('products:product_detail', slug=product.slug)
    else:
        form = ProductForm(instance=product)
        formset = ProductImageFormSet(instance=product)
    
    context = {
        'form': form,
        'formset': formset,
        'product': product,
        'title': f'Modifier le produit: {product.name}',
    }
    
    return render(request, 'products/product_form.html', context)


@login_required
def product_delete(request, slug):
    product = get_object_or_404(Product, slug=slug)
    
    if request.method == 'POST':
        product_name = product.name
        product.delete()
        messages.success(request, f'Le produit "{product_name}" a été supprimé avec succès.')
        return redirect('products:product_list')
    
    context = {
        'product': product,
        'title': f'Supprimer le produit: {product.name}',
    }
    
    return render(request, 'products/product_confirm_delete.html', context)
