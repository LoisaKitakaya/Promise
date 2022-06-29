from django.contrib import admin
from .models import Product, Category, Collection, Currency

# Register your models here.
@admin.register(Product)
class ProductAdminView(admin.ModelAdmin):

    model = Product

    list_display = (
        'name',
        'price',
        'category',
        'collection',
    )

    list_filter = (
        'category',
        'collection',
    )

    prepopulated_fields = {"slug": ("name",)}

@admin.register(Category)
class CategoryAdminView(admin.ModelAdmin):

    model = Category

    prepopulated_fields = {"slug": ("name",)}

@admin.register(Collection)
class CollectionAdminView(admin.ModelAdmin):

    model = Collection

    prepopulated_fields = {"slug": ("name",)}

@admin.register(Currency)
class CurrencyAdminView(admin.ModelAdmin):

    model = Currency
