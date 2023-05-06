from rest_framework import generics
from orders.models import Order, OrderArticle
from orders.serializers import OrderSerializer
from django.db import transaction
from orders.models import Article

class OrderCreate(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        with transaction.atomic():
            order_articles_data = self.request.data.pop('order_articles')
            total_price_excluding_tax = 0
            total_price_including_tax = 0

            for article_data in order_articles_data:
                article = Article.objects.get(id=article_data['article_id'])
                price_excluding_tax = article.price_excluding_tax * article_data['quantity']
                applicable_tax = article.applicable_tax
                price_including_tax = price_excluding_tax * (1 + applicable_tax / 100)
                total_price_excluding_tax += price_excluding_tax
                total_price_including_tax += price_including_tax
                article_data['price_excluding_tax'] = price_excluding_tax
                article_data['price_including_tax'] = price_including_tax

            order = Order.objects.create(total_price_excluding_tax=total_price_excluding_tax,
                                         total_price_including_tax=total_price_including_tax)

            for article_data in order_articles_data:
                OrderArticle.objects.create(order=order, **article_data)
