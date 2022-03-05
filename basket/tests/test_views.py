from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from store.models import Product, Category

class TestBasketView(TestCase):
    def setUp(self) -> None:
        #setup the database
        Category.objects.create(name='item', slug = 'item')
        User.objects.create(username='admin')
        Product.objects.create(category_id=1, created_by_id=1, title='new Prod 1', slug='new-prod-1',
                                        image='pic.png', price=30)
        Product.objects.create(category_id=1, created_by_id=1, title='new Prod 2', slug='new-prod-2',
                                        image='pic.png', price=30) 
        Product.objects.create(category_id=1, created_by_id=1, title='new Prod 3', slug='new-prod-3',
                                        image='pic.png', price=30)
        #add to the basket
        self.client.post(
            reverse('basket:basket_add'), {'productid': 1, 'productqty': 1, 'action': 'post'}, xhr=True
        )
        self.client.post(
            reverse('basket:basket_add'), {'productid': 2, 'productqty': 2, 'action': 'post'}, xhr=True
        )
        
    def test_basket_url(self):
        '''
        Test Homepage response status
        '''
        response = self.client.get(reverse('basket:basket_summary'))
        self.assertEqual(response.status_code, 200)

    def test_basket_add(self):
        '''
        Test Hadd item to the basket
        '''
        #case item is not in the basket
        response =    self.client.post(
            reverse('basket:basket_add'), {'productid': 3, 'productqty': 1, 'action': 'post'}, xhr=True
            )
        self.assertEqual(response.json(), {'qty':4}) #count all items added to the basket

        #case item is in the basket => replaces the qty of the product
        response =    self.client.post(
            reverse('basket:basket_add'), {'productid': 2, 'productqty': 1, 'action': 'post'}, xhr=True
            )
        self.assertEqual(response.json(), {'qty':3}) #the item 2 qty is updated from 2 to 1

    def test_basket_delete(self):
        '''
        Test deleting item from the basket
        '''
        response =    self.client.post(
            reverse('basket:basket_delete'), {'productid': 1, 'action': 'delete'}, xhr=True)
        
        self.assertEqual(response.json(),{'qty':2, 'subtotal':'60.00'})

    def test_basket_updatet(self):
        '''
        Test deleting item from the basket
        '''
        response =    self.client.post(
            reverse('basket:basket_update'), {'productid': 2, 'productqty': 2, 'action': 'update'}, xhr=True)
        
        self.assertEqual(response.json(),{'qty':3, 'subtotal':'90.00'})