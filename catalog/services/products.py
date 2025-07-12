from django.core.cache import cache
from catalog.models import Product

def get_products_by_category(category_id):
    key = f"products_category_{category_id}"
    products = cache.get(key)
    if products is None:
        products = list(Product.objects.filter(category_id=category_id))
        cache.set(key, products, 60 * 15)  # кеш на 15 минут
    return products
