from json import JSONDecodeError
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .basket import Basket
from store.models import Product

# Create your views here.

def basket_summary(request):
    return render(request, 'store/basket/summary.html')

def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action')=='post':
        product_id = int(request.POST.get('productid'))
        product = get_object_or_404(Product, id = product_id)
        product_qty = int(request.POST.get('productqty'))
        basket.add(product = product, qty = product_qty)
        basket_qty = basket.__len__()
        response = JsonResponse({'qty':basket_qty})
        return response

#we can use one method and then pass different action
def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action')=='delete':
        product_id = int(request.POST.get('productid'))
        basket.delete(productid=product_id)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty':basketqty, 'subtotal':baskettotal})
        # response = JsonResponse({'success':True})
        return response

#we can use one method and then pass different action
def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action')=='update':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        basket.update(productid=product_id, productqty = product_qty)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()

        # print('product_id', product_qty)
        # print(product_id, 'product_qty')
        response = JsonResponse({'qty':basketqty, 'subtotal':baskettotal})
        return response