from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.db.models import F,Sum
from decimal import Decimal

class Category(models.Model):
    # Description of a product. Fertilizer, feeds, etc.
    category_name = models.CharField(max_length=100,db_index=True)
    category_slug = models.SlugField(max_length=110,db_index=True,unique=True)
    category_description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('category_name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.category_name
    
    def save(self, *args, **kwargs):
        self.category_slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

class Product(models.Model):
    product_category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    product_code = models.CharField(max_length=20, db_index=True, unique=True)
    product_name = models.CharField(max_length=100, db_index=True)
    product_slug = models.SlugField(max_length=110, db_index=True)
    product_description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('product_name',)
        index_together = (('id', 'product_slug'),)
    def __str__(self):
        return self.product_name
    
    def save(self, *args, **kwargs):
        self.product_slug = slugify(self.product_name)
        super(Product, self).save(*args, **kwargs)
    
    def get_total_stock_quantity(self):
        total_quantity = 0

        # Calculate the total stock quantity for the product
        product_stocks = self.stock.all()  # Assuming you have related_name='stock' in ProductStock
        for stock in product_stocks:
            total_quantity += stock.product_quantity

        return total_quantity

    def get_remaining_stock(self):
        total_quantity = self.get_total_stock_quantity()
        products_issued_sum = self.stock.aggregate(Sum('products_issued'))['products_issued__sum']
        remaining_stock = total_quantity - products_issued_sum

        return remaining_stock
    
    def calculate_total_stock_value(self):
        total_stock_value = 0

        for product_stock in self.stock.all():
            remaining_stock = product_stock.product_quantity - product_stock.products_issued
            stock_value = remaining_stock * product_stock.product_bought_at
            total_stock_value += stock_value

        return total_stock_value