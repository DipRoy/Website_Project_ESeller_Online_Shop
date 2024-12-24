import unittest
from products.models import *


class TestModels(unittest.TestCase):

    def test_Models(self):
        product = Product.objects.create(
            product_id=18,
            product_name="Mango",
            category="Fruit",
            price=350,
            description="Fresh Mangoes",
            pub_date="2022-02-18",
        )

        self.assertEqual(str(product), "Mango")
        print("Unit testing 9: Unit testing for product model passed")


if __name__ == "__main__":
    unittest.main()