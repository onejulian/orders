from django.db import models

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    reference = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price_excluding_tax = models.DecimalField(max_digits=10, decimal_places=2)
    applicable_tax = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'articles'

    def __str__(self):
        return self.name
