import json
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from orders.models import Order, OrderArticle, Article
from orders.serializers import OrderSerializer

class OrderCreateTests(APITestCase):
    def setUp(self):
        self.url = reverse('order_create')

        self.article1 = Article.objects.create(
            name='Arroz',
            price_excluding_tax=100.0,
            applicable_tax=10,
            reference='ARROZ-001',
            description='Arroz de alta calidad.',
        )
        self.article2 = Article.objects.create(
            name='Frijoles',
            price_excluding_tax=200.0,
            applicable_tax=20,
            reference='FRIJ-001',
            description='Frijoles de alta calidad.',
        )

    def test_create_order(self):
        data = {
            'order_articles': [
                {
                    'article_id': self.article1.id,
                    'article_reference': self.article1.reference,
                    'quantity': 2,
                },
                {
                    'article_id': self.article2.id,
                    'article_reference': self.article2.reference,
                    'quantity': 1,
                },
            ],
        }

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        