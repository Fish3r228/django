from django.shortcuts import render
from catalog.services.products import get_products_by_category

def products_by_category(request, category_id):
    products = get_products_by_category(category_id)
    return render(request, 'products_by_category.html', {'products': products})
