from rest_framework import generics
from orders.models import Order, OrderArticle, Article
from orders.serializers import OrderSerializer, OrderArticleDetailSerializer, OrderDetailSerializer
from django.db import transaction
from rest_framework.response import Response

class OrderUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_order_articles(self, order):
        order_articles = OrderArticle.objects.filter(order=order)
        return order_articles

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        with transaction.atomic():
            order_articles_data = request.data.pop('order_articles')
            total_price_excluding_tax = 0
            total_price_including_tax = 0

            # Borrar los OrderArticles existentes
            # instance.order_articles.all().delete()
            order_articles = self.get_order_articles(instance)
            order_articles.delete()

            for article_data in order_articles_data:
                article = Article.objects.get(id=article_data['article_id'])
                price_excluding_tax = article.price_excluding_tax * article_data['quantity']
                applicable_tax = article.applicable_tax
                price_including_tax = price_excluding_tax * (1 + applicable_tax / 100)
                total_price_excluding_tax += price_excluding_tax
                total_price_including_tax += price_including_tax
                article_data['price_excluding_tax'] = price_excluding_tax
                article_data['price_including_tax'] = price_including_tax

            instance.total_price_excluding_tax = total_price_excluding_tax
            instance.total_price_including_tax = total_price_including_tax
            instance.save()

            for article_data in order_articles_data:
                OrderArticle.objects.create(order=instance, **article_data)

        # serializer = self.get_serializer(instance)
        order = self.get_object()
        serializer = OrderDetailSerializer(order)
        order_articles = self.get_order_articles(order)
        order_articles_serializer = OrderArticleDetailSerializer(order_articles, many=True)
        # return Response(serializer.data)      
        return Response({'order': serializer.data, 'order_articles': order_articles_serializer.data})