from django import forms
from .models import Category,Product

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'category_description']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_category','product_code','product_name','product_description']