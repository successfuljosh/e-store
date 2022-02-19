from django.urls import path
from . import views

app_name = 'store'      #matches namespace in the homepage

urlpatterns = [
    path('', views.all_products, name='all_products'),   #homepage
    path('about/', views.about_us, name='about_us'),
    path('item/<slug:product_slug>/', views.product_detail, name='product_detail'), #<datatype:variablename> ==> get parameter
    path('search/<slug:category_slug>/', views.category_list, name='category_list')  #<datatype:variablename> ==> get parameter
]