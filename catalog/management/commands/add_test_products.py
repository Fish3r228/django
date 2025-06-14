from django.core.management.base import BaseCommand
from catalog.models import Product, Category
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Загружает тестовые данные из фикстур'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()
        call_command('loaddata', 'categories.json')
        call_command('loaddata', 'products.json')
        self.stdout.write(self.style.SUCCESS('Тестовые данные загружены!'))
#