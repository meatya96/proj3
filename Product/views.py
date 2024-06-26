from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from Product.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ("name", "description", "price", "category", "photo")
    success_url = reverse_lazy("Product:product_list")


class ProductUpdateView(UpdateView):
    model = Product
    fields = ("name", "description", "price", "category", "photo")
    success_url = reverse_lazy("Product:product_list")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("Product:product_list")