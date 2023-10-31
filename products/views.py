from django.shortcuts import render, redirect,get_object_or_404
from .models import Category, Product
from .forms import CategoryForm, ProductForm  # Create a form for adding categories


def list_categories(request):
    categories = Category.objects.all()
    return render(request, 'products/list_categories.html', {'categories': categories})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:list_categories')
    else:
        form = CategoryForm()
    return render(request, 'products/add_category.html', {'form': form})

def update_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('products:list_categories')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'products/update_category.html', {'form': form, 'category': category})

def delete_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    category.delete()
    return redirect('products:list_categories')

def list_products(request):
    products = Product.objects.all()
    return render(request, 'products/list_products.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:list_products')
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})

def update_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:list_products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/update_product.html', {'form': form, 'product': product})

def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect('products:list_products')