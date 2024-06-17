from django.urls import path
from Product.apps import ProductConfig

from Product.views import product_list, single_product

app_name = ProductConfig.name

urlpatterns = [
    path('', product_list, name='product_list'),
    path('product/<int:pk>/', single_product, name='single_product')
]
