from django.contrib import admin
from products.models import Category,Product

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['category_name']
    list_display = ["category_name",'date_created','date_updated']
    prepopulated_fields = {"category_slug": ("category_name",)}

class ProductAdmin(admin.ModelAdmin):
    search_fields = ['product_name']
    list_display = ['product_code','product_name','product_category','date_created','date_updated']
    list_filter = ['product_category','date_updated','date_created']
    prepopulated_fields = {"product_slug": ("product_name",)}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)