from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=120)
    desc = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(blank=True, null=False)
    featured = models.BooleanField()

