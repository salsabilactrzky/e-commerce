from django.test import TestCase, Client
from django.utils import timezone
from django.urls import reverse
from .models import Product

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get(reverse('main:show_main'))
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get(reverse('main:show_main'))
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_product_is_sold(self):
        self.product.stock = 0
        self.product.save()
        self.assertTrue(self.product.is_sold)

    def test_product_is_not_sold(self):
        self.assertFalse(self.product.is_sold)