from django.db import models
from products.models import Product

# Create your models here.
class Review(models.Model):

    headline = models.CharField(blank=False, max_length=200)
    name = models.CharField(blank=False, max_length=200)
    email = models.EmailField(blank=False, max_length=200, unique=True)
    content = models.TextField()
    rating = models.IntegerField(default=0, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)