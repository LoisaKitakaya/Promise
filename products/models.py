from django.db import models

# Create your models here.
class Currency(models.Model):

    code = models.CharField(blank=False, unique=True, max_length=200)
    default = models.BooleanField(blank=False, default=False)
    rate = models.FloatField(blank=False, default=0.0)

    def __str__(self) -> str:
        
        return self.code

class Category(models.Model):

    name = models.CharField(blank=False, max_length=200)
    slug = models.SlugField(blank=False, max_length=200, unique=True)
    description = models.TextField()

    def __str__(self) -> str:
        
        return self.name

class Collection(models.Model):

    name = models.CharField(blank=False, max_length=200)
    slug = models.SlugField(blank=False, max_length=200, unique=True)
    description = models.TextField()

    def __str__(self) -> str:
        
        return self.name

class Product(models.Model):

    name = models.CharField(blank=False, max_length=200, unique=True)
    slug = models.SlugField(blank=False, unique=True, max_length=200)
    description = models.TextField()
    price = models.IntegerField(blank=False, default=0)
    image = models.URLField(blank=False, max_length=254)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    def __str__(self) -> str:
        
        return self.name