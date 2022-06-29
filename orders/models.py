from django.db import models

# Create your models here.
class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    sub_total = models.CharField(blank=False, max_length=200)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.first_name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.CharField(blank=False, max_length=200)
    quantity = models.CharField(blank=False, max_length=200)
    total = models.CharField(blank=False, max_length=200)
    
    def __str__(self):
        return self.product