from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.


def index(request):
    products = Product.objects.filter(is_available=True)
    context = {
       'products':products
    }
    return render(request, "product/index.html", context)

def store(request, category_slug=None):
    print("== 1 ==")
    if category_slug == None:
        products = Product.objects.filter(is_available=True)
    else:
        print("== 2 ==")
        categories = get_object_or_404(Category, slug=category_slug)
        print("== 3 ==")
        products = Product.objects.filter(is_available=True, category=categories)
        print("== 4 ==")
    context = {
        'products': products,
        'product_count': products.count()
    }
    return render(request, 'product/store.html', context)

def product_detail(request, category_slug, product_slug):
    product = get_object_or_404(Product,slug=product_slug, category__slug=category_slug)
        
    context = {
        'product': product
    }
    return render(request, 'product/product-detail.html', context)
