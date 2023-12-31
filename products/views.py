from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from inventory.models import ProductStock
from .models import Category, Product
from .forms import CategoryForm, ProductForm  # Create a form for adding categories

@login_required(login_url='/')
def list_categories(request):
    categories = Category.objects.all()
    return render(request, 'products/list_categories.html', {'categories': categories})

@login_required(login_url='/')
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:list_categories')
    else:
        form = CategoryForm()
    return render(request, 'products/add_category.html', {'form': form})

@login_required(login_url='/')
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

@login_required(login_url='/')
def delete_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    category.delete()
    return redirect('products:list_categories')

@login_required(login_url='/')
def list_products(request):
    products = Product.objects.all()
    return render(request, 'products/list_products.html', {'products': products})

@login_required(login_url='/')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:list_products')
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})

@login_required(login_url='/')
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

@login_required(login_url='/')
def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect('products:list_products')

@login_required(login_url='/')
def product_detail(request,product_id):
    product = get_object_or_404(Product, pk=product_id)
    stocks = ProductStock.objects.filter(product=product,stock_finished=False)
    return render(request, 'products/product_detail.html', {'product': product,'stocks':stocks})

def index(request):
    return render(request, 'products/index.html')
    