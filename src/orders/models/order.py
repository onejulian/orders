from django.db import models
from orders.models.article import Article

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    total_price_excluding_tax = models.DecimalField(max_digits=10, decimal_places=2)
    total_price_including_tax = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return f'Order {self.id}'

class OrderArticle(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    article_reference = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price_excluding_tax = models.DecimalField(max_digits=10, decimal_places=2)
    price_including_tax = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'order_articles'

    def __str__(self):
        return f'Order article {self.id}'
