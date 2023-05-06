from rest_framework import generics
from orders.models import Article
from orders.serializers import ArticleSerializer

class ArticleCreate(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
