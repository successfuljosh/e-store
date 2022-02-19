from math import prod
from unicodedata import category
from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponse
from .models import Product, Category


def get_categories(request):
    return {
        'categories': Category.objects.all()
    }

def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

def about_us(request):
    return render(request, 'store/about.html')

def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug, in_stock=True)
    return render(request, 'store/products/detail.html', {'product': product})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug = category_slug)
    products = Product.objects.filter(category = category)
    return render(request, 'store/products/category.html',{'category':category, 'products':products})