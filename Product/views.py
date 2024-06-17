from django.shortcuts import render

from Product.models import Product


def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'product/product_list.html', context)


def single_product(request, pk):
    product = Product.objects.get(pk=pk)
    context = {"product": product}
    return render(request, 'product/single_product.html', context)
