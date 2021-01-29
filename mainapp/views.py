from django.shortcuts import render

from mainapp.models import Product, ProductCategory


def index(request):
    content = {
        'title': 'GeekShop'
    }
    return render(request, 'mainapp/index.html', content)


def products(request):
    content = {
        'title': 'GeekShop - Категории',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),

    }
    return render(request, 'mainapp/products.html', content)