import unittest
from django.test import  Client
from django.urls import reverse
from django.contrib.auth.models import User
from checkout.models import *

class TestViews(unittest.TestCase):

        def test_customer_authentication(self):
            password = 'mypassword'
            my_admin = User.objects.create_superuser('Ashraful', 'myemail@test.com', password)
            c = Client()
            c.login(username=my_admin.username, password=password)
            print("Authentication passed")

class URLTests (unittest.TestCasetCase):
    
    def test_checkoutpage (self):
     
         response = self.client.get('checkout.html')
         self.assertEqual (response.status_code, 200)
         print("Unit testing for checkout page view passed")

class TestViews (unittest.TestCasetCase):

    def test_checkout(self):

         client = Client ()
         response = client.get(reverse('list'))
         self.assertEquals(response.status_code, 200)
         self.assertTemplateUsed (response, 'base/checkout.html')
         print("Unit testing for checkout page funtions passed")

         



