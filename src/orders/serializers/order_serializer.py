from rest_framework import serializers
from orders.models import Order, OrderArticle

class OrderArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderArticle
        fields = ['article_id', 'article_reference', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    order_articles = OrderArticleSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'order_articles']

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'total_price_excluding_tax', 'total_price_including_tax', 'created_at']
        depth = 1

class OrderArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderArticle
        fields = ['article_id', 'article_reference', 'quantity', 'price_excluding_tax', 'price_including_tax']
        depth = 1