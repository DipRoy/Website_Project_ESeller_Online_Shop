import unittest
from django.urls import reverse, resolve
from checkout.views import *


class TestUrls(unittest.TestCase):

    def test_checkout_is_resolved(self):
        url = reverse('checkout')
        self.assertEquals(resolve(url).func, CartProduct)
        print("Unit testing for fruit url passed")