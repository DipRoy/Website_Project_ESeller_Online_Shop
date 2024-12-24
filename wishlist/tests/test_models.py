import unittest
from wishlist.models import *


class TestModels(unittest.TestCase):

    def test_Models(self):
        wishlist = Wishlist.objects.create(
            category = "Fruit",
            product_name = "Mango",
            description = "Fresh Mangoes",
        )

        self.assertEqual(str(wishlist), "Fruit")
        print("Unit testing 2 : Unit testing for wishlist model passed")


if __name__ == "__main__":
    unittest.main()