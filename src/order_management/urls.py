from django.urls import path
from orders import views

urlpatterns = [
    path('articles/', views.ArticleCreate.as_view(), name='article_create'),
    path('orders/', views.OrderCreate.as_view(), name='order_create'),
    path('articles/<int:pk>/', views.ArticleDetail.as_view(), name='article_detail'),
    path('list-articles/', views.ArticleList.as_view(), name='article_list'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('list-orders/', views.OrderList.as_view(), name='order_list'),
    path('update-order/<int:pk>/', views.OrderUpdateView.as_view(), name='order-update'),  
]
