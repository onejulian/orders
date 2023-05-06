from django.contrib import admin
from orders.models.order import Order
from orders.models.order import OrderArticle
from orders.models.article import Article

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderArticle)
admin.site.register(Article)
