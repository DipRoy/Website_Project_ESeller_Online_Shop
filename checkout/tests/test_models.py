import unittest
from ESeller.user_dashboard.models import Customer
from checkout.models import *


class TestModels(unittest.TestCase):

    def test_Models(self):
        
        product = CartProduct.objects.create(
            customer="Ashraful",
            cart="productlist",
            product="Chocolate",
            quantity=50,
            subtotal=700,
            created_at="2022-04-18",
        )

        self.assertEqual(str(Customer), "Person1")
    print("Unit testing 9: Unit testing for product model passed")


if __name__ == "__main__":
    unittest.main()

