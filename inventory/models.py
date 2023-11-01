from django.db import models
from products.models import Product
from django.db.models.signals import pre_save
from django.dispatch import receiver

class ProductSupplier(models.Model):
    supplier_name = models.CharField(max_length=150,unique=True)
    supplier_description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('date_created',)
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'
    def __str__(self):
        return self.supplier_name


class ProductStock(models.Model):
    product_supplier = models.ForeignKey(ProductSupplier,related_name='supplier',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='stock',on_delete=models.CASCADE)
    product_quantity = models.IntegerField()
    products_issued = models.IntegerField(default=0)
    product_bought_at = models.DecimalField(max_digits=10, decimal_places=2)
    stock_finished = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-date_created',)
        verbose_name = 'Product Stock'
        verbose_name_plural = 'Product Stocks'
    
    def __str__(self):
        return self.product.product_name
    
    def update_stock_finished(self):
        if self.products_issued >= self.product_quantity:
            self.stock_finished = True
        else:
            self.stock_finished = False
    
    def save(self, *args, **kwargs):
        self.update_stock_finished()
        super().save(*args, **kwargs)
    
    def product_stock_amount(self):
        return self.product_bought_at * self.product_quantity

@receiver(pre_save, sender=ProductStock)
def update_stock_finished(sender, instance, **kwargs):
    instance.update_stock_finished()