from django.shortcuts import render

from product.models import Product, Category


def get_all_products(request):
    products = Product.objects.all()
    return render(request, "product/product.html", {"products": products})


def get_all_categories(request):
    categories = Category.objects.all()
    return render(request, "categories/categories.html", {"categories": categories})
