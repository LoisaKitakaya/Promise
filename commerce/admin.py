from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class ProductAdminView(admin.ModelAdmin):

    model = Product

    list_display = (
        'name',
        'description',
    )
