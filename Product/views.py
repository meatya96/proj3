from django.shortcuts import render

from Product.models import Product


def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'product_list.html', context)