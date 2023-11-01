from django.urls import path
from . import views

app_name = 'inventory'
urlpatterns = [
    path('list-suppliers/',views.list_suppliers,name='list_suppliers'),
    path('add-supplier/',views.add_supplier,name='add_supplier'),
    path('update-supplier/<int:supplier_id>/', views.update_supplier, name='update_supplier'),
    path('delete-supplier/<int:supplier_id>/',views.delete_supplier,name='delete_supplier'),
    # stock
    path('add-stock/<int:product_id>/',views.add_product_stock,name='add_product_stock'),
]
