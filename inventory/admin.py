from django.contrib import admin
from .models import ProductSupplier,ProductStock

class ProductSupplierAdmin(admin.ModelAdmin):
    list_display = ['supplier_name','supplier_description','date_created','date_updated']
    list_filter = ['date_updated','date_created']

class ProductStockAdmin(admin.ModelAdmin):
    list_display = ['product','product_supplier','product_quantity',
                    'products_issued','product_bought_at','stock_finished','date_created']
    list_filter = ['product','product_supplier','date_created']
    

admin.site.register(ProductSupplier, ProductSupplierAdmin)
admin.site.register(ProductStock, ProductStockAdmin)
