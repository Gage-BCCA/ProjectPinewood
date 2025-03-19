from django.test import TestCase
from storefront.models import *

class ProductTestCase(TestCase):

    def test_product_creation(self):
        Product.objects.create(
            listing_id = 1,
            title = "Test Product",
            description = "For Testing Products",
            price = 19.99 ,
            currency_code = "USD",
            quantity = 3,
            url = "https://example.com/test",
            shop_id = 2000,
            shop_name = "Test Shop",
            created_at = 0,
            is_active = True,
        )

        target_product = Product.objects.get(title="Test Product")
        self.assertIsNotNone(target_product)
        self.assertIsInstance(target_product, Product)
        self.assertEqual(target_product.title, "Test Product")
        