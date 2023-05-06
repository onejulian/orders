from rest_framework import serializers
from orders.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'reference', 'name', 'description', 'price_excluding_tax', 'applicable_tax', 'created_at']
