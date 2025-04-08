from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from .models import Category
from .forms import CategoryForm


@login_required
def category_list(request):
    categories = Category.objects.annotate(product_count=Count('products'))
    
    context = {
        'categories': categories,
        'title': 'Liste des catégories',
    }
    
    return render(request, 'categories/category_list.html', context)


@login_required
def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    
    context = {
        'category': category,
        'products': products,
        'title': category.name,
    }
    
    return render(request, 'categories/category_detail.html', context)


@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save()
            messages.success(request, f'La catégorie "{category.name}" a été créée avec succès.')
            return redirect('categories:category_list')
    else:
        form = CategoryForm()
    
    context = {
        'form': form,
        'title': 'Ajouter une catégorie',
    }
    
    return render(request, 'categories/category_form.html', context)


@login_required
def category_update(request, slug):
    category = get_object_or_404(Category, slug=slug)
    
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            category = form.save()
            messages.success(request, f'La catégorie "{category.name}" a été mise à jour avec succès.')
            return redirect('categories:category_list')
    else:
        form = CategoryForm(instance=category)
    
    context = {
        'form': form,
        'category': category,
        'title': f'Modifier la catégorie: {category.name}',
    }
    
    return render(request, 'categories/category_form.html', context)


@login_required
def category_delete(request, slug):
    category = get_object_or_404(Category, slug=slug)
    
    if request.method == 'POST':
        category_name = category.name
        category.delete()
        messages.success(request, f'La catégorie "{category_name}" a été supprimée avec succès.')
        return redirect('categories:category_list')
    
    context = {
        'category': category,
        'title': f'Supprimer la catégorie: {category.name}',
    }
    
    return render(request, 'categories/category_confirm_delete.html', context)
