import unittest
from django.test import  Client
from django.urls import reverse
from django.contrib.auth.models import User
from products.models import *


class TestViews(unittest.TestCase):

    def test_fruit_GET(self):
        client = Client()
        response = client.get(reverse('products:fruit'))
        self.assertEquals(response.status_code, 200)
        print("Unit testing 10: Unit testing for fruit view passed")


    def test_vegetable_GET(self):
        client = Client()
        response = client.get(reverse('products:vegetable'))
        self.assertEquals(response.status_code, 200)
        print("Unit testing 11: Unit testing for fruit view passed")


    def test_fish_GET(self):
        client = Client()
        response = client.get(reverse('products:fish'))
        self.assertEquals(response.status_code, 200)
        print("Unit testing 12: Unit testing for fish view passed")


    def test_medicine_GET(self):
        client = Client()
        response = client.get(reverse('products:medicine'))
        self.assertEquals(response.status_code, 200)
        print("Unit testing 13: Unit testing for medicine view passed")


    def test_meat_GET(self):
        client = Client()
        response = client.get(reverse('products:meat'))
        self.assertEquals(response.status_code, 200)
        print("Unit testing 14: Unit testing for meat view passed")


    def test_add_product(self):
        password = 'mypassword'
        my_admin = User.objects.create_superuser('SUNJARE', 'myemail@test.com', password)
        c = Client()
        c.login(username=my_admin.username, password=password)

        product = Product.objects.create(
            product_id=199,
            product_name="Mango",
            category="Fruit",
            price=350,
            description="Fresh Mangoes",
            pub_date="2022-02-18",
        )

        client = Client()
        response = client.get(reverse('products:add_product'))
        self.assertEquals(response.status_code, 200)
        self.assertEqual(str(product), "Mango")
        print("Unit testing 15: Unit testing for add_product view passed")


    def test_update_product(self):
        password = 'mypassword'
        my_admin = User.objects.create_superuser('SUNJARE', 'myemail@test.com', password)
        c = Client()
        c.login(username=my_admin.username, password=password)

        product = Product.objects.create(
            product_id=29,
            product_name="Mango",
            category="Fruit",
            price=350,
            description="Fresh Mangoes",
            pub_date="2022-02-18",
        )

        product = Product.objects.get(pk=29)
        product.product_name = "Strawberry"

        client = Client()
        response = client.get(reverse('products:update_product'))
        self.assertEquals(response.status_code, 200)
        self.assertEqual(str(product), "Strawberry")
        print("Unit testing 16: Unit testing for update_product view passed")


    def test_delete_product(self):
        product = Product.objects.create(
            product_id=305,
            product_name="Mango",
            category="Fruit",
            price=350,
            description="Fresh Mangoes",
            pub_date="2022-02-18",
        )

        product = Product.objects.get(pk=305)
        product.delete()

        client = Client()
        response = client.get(reverse('products:delete_product'))
        self.assertEqual(Product.objects.filter(category="Fruit").count(), 0)
        self.assertEquals(response.status_code, 200)
        print("Unit testing 17: Unit testing for delete_product view passed")