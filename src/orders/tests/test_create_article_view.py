from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from orders.models import Article

class ArticleCreateTests(APITestCase):
    def setUp(self):
        self.url = reverse('article_create')

    def test_create_article(self):
        data = {
            "reference": "HUEVOS-001",
            "name": "Huevos de gallina",
            "description": "Paquete de 12 huevos de gallina frescos y de alta calidad.",
            "price_excluding_tax": 6000.00,
            "applicable_tax": 19.00,
        }

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        article = Article.objects.get(id=response.data['id'])
        self.assertEqual(article.name, data['name'])
        self.assertEqual(article.reference, data['reference'])
        self.assertEqual(article.description, data['description'])
        self.assertEqual(article.price_excluding_tax, data['price_excluding_tax'])
        self.assertEqual(article.applicable_tax, data['applicable_tax'])

