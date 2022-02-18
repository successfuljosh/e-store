from django.urls import path
from . import views

app_name = 'store'      #matches namespace in the homepage

urlpatterns = [
    path('', views.all_products, name='all_products'),   #homepage
]