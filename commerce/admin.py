from django.contrib import admin
from .models import Product, Category, Collection, ColorVarient, Currency, SizeVarient

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
        'color_varience',
        'size_varience',
    )

@admin.register(Category)
class CategoryAdminView(admin.ModelAdmin):

    model = Category

@admin.register(Collection)
class CollectionAdminView(admin.ModelAdmin):

    model = Collection

@admin.register(Currency)
class CurrencyAdminView(admin.ModelAdmin):

    model = Currency

@admin.register(ColorVarient)
class ColorVarientAdminView(admin.ModelAdmin):

    model = ColorVarient

@admin.register(SizeVarient)
class SizeVarientAdminView(admin.ModelAdmin):

    model = SizeVarient
