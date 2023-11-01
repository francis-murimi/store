from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import ProductSupplier, ProductStock
from .forms import ProductSupplierForm, ProductStockForm  # Create a form for adding categories

@login_required(login_url='/')
def list_suppliers(request):
    suppliers = ProductSupplier.objects.all()
    return render(request, 'inventory/list_suppliers.html', {'suppliers': suppliers})

@login_required(login_url='/')
def add_supplier(request):
    if request.method == 'POST':
        form = ProductSupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory:list_suppliers')
    else:
        form = ProductSupplierForm()
    return render(request, 'inventory/add_supplier.html', {'form': form})

@login_required(login_url='/')
def update_supplier(request, supplier_id):
    supplier = get_object_or_404(ProductSupplier, pk=supplier_id)
    if request.method == 'POST':
        form = ProductSupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('inventory:list_suppliers')
    else:
        form = ProductSupplierForm(instance=supplier)
    return render(request, 'inventory/update_supplier.html', {'form': form, 'supplier': supplier})

@login_required(login_url='/')
def delete_supplier(request, supplier_id):
    supplier = get_object_or_404(ProductSupplier, pk=supplier_id)
    supplier.delete()
    return redirect('inventory:list_suppliers')

@login_required(login_url='/')
def add_product_stock(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductStockForm(request.POST)
        if form.is_valid():
            product_stock = form.save(commit=False)
            product_stock.product = product  # Assign the product to the ProductStock instance
            product_stock.save()  # Save the ProductStock with the associated product
            return redirect('products:list_products')
    else:
        form = ProductStockForm()
    return render(request, 'inventory/add_stock.html', {'form': form})