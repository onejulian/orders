from orders.models import Order
from orders.serializers import OrderDetailSerializer, OrderArticleDetailSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from orders.models import Order, OrderArticle

class OrderList(APIView):
        
    def get_orders(self):
        orders = Order.objects.all()
        return orders
        
    def get_order_articles(self, order):
        order_articles = OrderArticle.objects.filter(order_id=order.id)
        return order_articles

    def get(self, request, format=None):
        orders = self.get_orders()
        list_orders = []
        for order in orders:
            serializer = OrderDetailSerializer(order)
            order_articles = self.get_order_articles(order)
            order_articles_serializer = OrderArticleDetailSerializer(order_articles, many=True)
            list_orders.append({'order': serializer.data, 'order_articles': order_articles_serializer.data})
        return Response({'orders': list_orders})
