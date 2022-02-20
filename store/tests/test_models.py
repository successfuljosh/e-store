from unicodedata import category

from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Category, Product


# Create your tests here.
class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name='item', slug = 'item')

    def test_category_entry_model(self):
        """
        Test category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))  #this test if the model data is properly created
   
    def test_category_entry_model(self):
        """
        Test category model string name.. test that the db returns the correct value
        """
        data = self.data1
        self.assertEqual(str(data), 'item')

class TestProductsModel(TestCase):
    def setUp(self):
        #product require category and user createed
        Category.objects.create(name='item', slug = 'item')
        User.objects.create(username='admin')
        self.data1 =Product.objects.create(category_id=1, created_by_id=1, title='new Prod', slug='new-prod',
                                        image='pic.png', price=30.26)

    def test_product_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data),'new Prod')
