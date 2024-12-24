import unittest
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from wishlist.models import *


class TestViews(unittest.TestCase):

    def test_wishlist(self):

        wishlist = Wishlist.objects.create( 
            category = "Fruit",
            name = "Mango",
            description = "Fresh Mangoes",
        )

        client = Client()
        response = client.get(reverse('wishlist:wishlist'))
        self.assertEquals(response.status_code, 200)
        print("Unit testing 1 : Unit testing for wishlist view passed")
        

