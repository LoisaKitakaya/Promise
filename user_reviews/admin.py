from django.contrib import admin
from .models import Review

# Register your models here.
@admin.register(Review)
class ReviewAdminView(admin.ModelAdmin):

    model = Review

    list_display = (
        'headline',
        'email',
        'rating',
    )

    list_filter = (
        'product',
    )