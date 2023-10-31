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