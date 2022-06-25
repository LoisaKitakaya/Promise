from django.db import models

# Create your models here.
class Product(models.Model):

    name = models.CharField(blank=False, max_length=200, verbose_name='product name')

    description = models.TextField()

    def __str__(self) -> str:
        
        return self.name