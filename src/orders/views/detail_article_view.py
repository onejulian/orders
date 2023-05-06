from rest_framework import generics
from orders.models import Article
from orders.serializers import ArticleSerializer

class ArticleDetail(generics.RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
