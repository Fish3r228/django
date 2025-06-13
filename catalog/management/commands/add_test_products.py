from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Удаляет все данные и добавляет тестовые категории и продукты'

    def handle(self, *args, **kwargs):
        self.stdout.write('Удаляем все существующие данные...')
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write('Добавляем тестовые категории...')
        cat1 = Category.objects.create(name='Electronics', description='Electronic gadgets')
        cat2 = Category.objects.create(name='Books', description='All kinds of books')

        self.stdout.write('Добавляем тестовые продукты...')
        Product.objects.create(name='Smartphone', description='A cool smartphone', category=cat1, price=699.99)
        Product.objects.create(name='Laptop', description='Powerful laptop', category=cat1, price=1299.99)
        Product.objects.create(name='Novel', description='Interesting novel book', category=cat2, price=19.99)

        self.stdout.write(self.style.SUCCESS('Тестовые данные успешно добавлены.'))
#1