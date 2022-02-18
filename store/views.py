from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category


def get_categories(request):
    return {
        'categories': Category.objects.all()
    }

def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})
