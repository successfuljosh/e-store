#pep8... separating the import sections
from importlib import import_module
from unittest import skip

from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse
from django.conf import settings

from store.models import Category, Product
from store.views import all_products


# Create your tests here.
#Skipping test reminds you of a test to perform instead of just commenting the test
@skip("demonstrating skipping")
class TestSkip(TestCase):
    def test_skip_example(self):
        pass

    

class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()


        #url requires data in the db
        Category.objects.create(name='item', slug = 'item')
        User.objects.create(username='admin')
        self.data1 =Product.objects.create(category_id=1, created_by_id=1, title='new Prod', slug='new-prod',
                                        image='pic.png', price=30.26)

    def test_url_allowed_hosts(self):
        """
        Test response from homepage and about page
        """
        res = self.c.get('/', HTTP_HOST = 'noadress.com')
        self.assertEqual(res.status_code, 400) #status code for not allowed
        res = self.c.get('/', HTTP_HOST = 'yourdomain.com')
        self.assertEqual(res.status_code, 200) #status code for successful response
        #test about page
        res = self.c.get('/about/')
        self.assertEqual(res.status_code, 200) #status code for successful response
           
    def test_product_detail_url(self):
        """
        Test product detail view
        """
        res = self.c.get(reverse("store:product_detail", args=['new-prod']))
        self.assertEqual(res.status_code, 200)

    def test_category_detail_url(self):
        """
        Test product detail view
        """
        res = self.c.get(reverse("store:category_list", args=['item']))
        self.assertEqual(res.status_code, 200)

    #test the content of the html
    def test_homepage_html(self):
        req = HttpRequest()
        #added the session feature to the test
        engine = import_module(settings.SESSION_ENGINE)
        req.session = engine.SessionStore()
        response = all_products(req)
        html = response.content.decode('utf-8')
        # print(html)
        self.assertIn('<title>E-Store Home</title>', html)
        self.assertTrue(html.startswith('\n<!doctype html>\n'))
        self.assertEqual(response.status_code, 200)
    
    # def test_view_function(self):
    #     request = self.factory.get('/new-prod/')
    #     response = all_products(request)
    #     html = response.content.decode('utf-8')
    #     self.assertIn('<title>E-Store Home</title>', html)
    #     self.assertTrue(html.startswith('\n<!doctype html>\n'))
    #     self.assertEqual(response.status_code, 200)