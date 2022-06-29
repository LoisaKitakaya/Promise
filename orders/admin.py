from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.
@admin.register(Order)
class ProductAdminView(admin.ModelAdmin):

    model = Order

    list_display = (
        'first_name',
        'email',
    )

    list_filter = (
        'created_at',
    )

@admin.register(OrderItem)
class CategoryAdminView(admin.ModelAdmin):

    model = OrderItem

    list_display = (
        'product',
        'quantity',
    )

    list_filter = (
        'order',
    )