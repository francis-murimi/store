from django import forms
from .models import ProductSupplier,ProductStock

class ProductSupplierForm(forms.ModelForm):
    class Meta:
        model = ProductSupplier
        fields = ['supplier_name', 'supplier_description']

class ProductStockForm(forms.ModelForm):
    class Meta:
        model = ProductStock
        fields = ['product_supplier','product_quantity','product_bought_at',]