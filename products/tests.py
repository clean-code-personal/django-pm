from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Product


class ProductModelTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            description="A test product description",
            price=10.00,
            stock=100
        )

    def test_product_created(self):
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.description, "A test product description")
        self.assertEqual(self.product.price, 10.00)
        self.assertEqual(self.product.stock, 100)

    def test_product_string_representation_is_the_name(self):
        self.assertEqual(str(self.product), "Test Product")


class ProductAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product_data = {
            "name": "API Product",
            "description": "API Product Description",
            "price": 15.00,
            "stock": 50
        }
        self.product = Product.objects.create(**self.product_data)
        self.url = reverse('product-list')  # This will use the router to get the 'list' view

    def test_get_product_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_create_product(self):
        response = self.client.post(self.url, {
            "name": "New API Product",
            "description": "New product description",
            "price": 20.00,
            "stock": 30
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)  # 1 existing product + 1 new product

    def test_get_single_product(self):
        product_detail_url = reverse('product-detail', kwargs={'pk': self.product.id})
        response = self.client.get(product_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.product_data['name'])

    def test_update_product(self):
        product_detail_url = reverse('product-detail', kwargs={'pk': self.product.id})
        response = self.client.put(product_detail_url, {
            "name": "Updated Product",
            "description": "Updated description",
            "price": 25.00,
            "stock": 75
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, "Updated Product")
        self.assertEqual(self.product.price, 25.00)

    def test_delete_product(self):
        product_detail_url = reverse('product-detail', kwargs={'pk': self.product.id})
        response = self.client.delete(product_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)
