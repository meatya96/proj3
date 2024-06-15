from django.urls import path
from Product.apps import ProductConfig

from Product.views import product_list
app_name = ProductConfig.name

urlpatterns = [
    path('', product_list)
]
