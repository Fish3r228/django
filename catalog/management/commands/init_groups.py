from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product

class Command(BaseCommand):
    """
    Команда для создания группы 'Модератор продуктов' и назначения ей прав:
    - удаление продуктов;
    - снятие публикации с продукта.
    """
    help = 'Создаёт группу Модераторов продуктов и назначает права'

    def handle(self, *args, **kwargs):
        """
        Основной метод, выполняющий создание группы и добавление прав.
        """
        group, created = Group.objects.get_or_create(name='Модератор продуктов')

        content_type = ContentType.objects.get_for_model(Product)

        # Права
        perms = [
            Permission.objects.get(codename='can_unpublish_product'),
            Permission.objects.get(codename='delete_product'),
        ]

        for perm in perms:
            group.permissions.add(perm)

        self.stdout.write(self.style.SUCCESS('Группа Модератор продуктов создана и права назначены'))
