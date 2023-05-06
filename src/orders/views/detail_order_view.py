from orders.models import Order, OrderArticle
from orders.serializers import OrderDetailSerializer, OrderArticleDetailSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

class OrderDetailView(APIView):
    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404
        
    def get_order_articles(self, order):
        order_articles = OrderArticle.objects.filter(order_id=order.id)
        return order_articles

    def get(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = OrderDetailSerializer(order)
        order_articles = self.get_order_articles(order)
        order_articles_serializer = OrderArticleDetailSerializer(order_articles, many=True)
        return Response({'order': serializer.data, 'order_articles': order_articles_serializer.data})

