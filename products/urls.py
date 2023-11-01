from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('list-category/',views.list_categories,name='list_categories'),
    path('add-category/',views.add_category,name='add_category'),
    path('update-category/<int:category_id>/', views.update_category, name='update_category'),
    path('delete-category/<int:category_id>/',views.delete_category,name='delete_category'),
    # products
    path('list-product/',views.list_products,name='list_products'),
    path('add-product/',views.add_product,name='add_product'),
    path('update-product/<int:product_id>/', views.update_product, name='update_product'),
    path('delete-product/<int:product_id>/',views.delete_product,name='delete_product'),
    path('detail/<int:product_id>/',views.product_detail,name='product_detail'),
]
