import unittest
from django.urls import reverse, resolve
from products.views import *


class TestUrls(unittest.TestCase):

    def test_fruit_url_is_resolved(self):
        url = reverse('products:fruit')
        self.assertEquals(resolve(url).func, fruit)
        print("Unit testing 1: Unit testing for fruit url passed")

    def test_vegetable_url_is_resolved(self):
        url = reverse('products:vegetable')
        self.assertEquals(resolve(url).func, vegetable)
        print("Unit testing 2: Unit testing for vegetable url passed")

    def test_medicine_url_is_resolved(self):
        url = reverse('products:medicine')
        self.assertEquals(resolve(url).func, medicine)
        print("Unit testing 3: Unit testing for medicine url passed")

    def test_meat_url_is_resolved(self):
        url = reverse('products:meat')
        self.assertEquals(resolve(url).func, meat)
        print("Unit testing 4: Unit testing for meat url passed")

    def test_fish_url_is_resolved(self):
        url = reverse('products:fish')
        self.assertEquals(resolve(url).func, fish)
        print("Unit testing 5: Unit testing for fish url passed")

    def test_add_product_url_is_resolved(self):
        url = reverse('products:add_product')
        self.assertEquals(resolve(url).func, add_product)
        print("Unit testing 6: Unit testing for add_product url passed")

    def test_update_product_url_is_resolved(self):
        url = reverse('products:update_product', args=[1])
        self.assertEquals(resolve(url).func, update_product)
        print("Unit testing 7: Unit testing for update_product url passed")

    def test_delete_product_url_is_resolved(self):
        url = reverse('products:delete_product', args=[1])
        self.assertEquals(resolve(url).func, delete_product)
        print("Unit testing 8: Unit testing for delete_product url passed")


if __name__ == "__main__":
    unittest.main()