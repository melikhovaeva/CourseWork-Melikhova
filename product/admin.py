from django.contrib import admin

from product.models import Category, Product

admin.site.register(Category)
@admin.register(Product)

class AdminProduct (admin.ModelAdmin):
    list_display = ("name", "category", "weight", "price")
