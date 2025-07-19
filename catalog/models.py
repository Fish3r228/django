from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

BAD_WORDS = ['дурак', 'плохой', 'запрещено']

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        """
        Метаданные модели:
        - verbose_name и verbose_name_plural: человекочитаемые названия;
        - custom permissions: разрешение can_unpublish_product.
        """
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        """
        Строковое представление объекта продукта (его имя).
        """
        return self.name

class Product(models.Model):
    """
    Модель товара.

    Атрибуты:
    - name: название продукта;
    - description: описание;
    - image: изображение;
    - price: цена;
    - created_at: дата создания;
    - updated_at: дата обновления;
    - is_available: доступность;
    - is_published: опубликован ли;
    - owner: владелец (пользователь).
    """
    is_available = models.BooleanField(default=True, verbose_name="Доступен ли товар")
    is_published = models.BooleanField(default=False, verbose_name="Опубликован")

    name = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='products/', verbose_name='Изображение', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Владелец'
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()
        for bad_word in BAD_WORDS:
            if bad_word.lower() in self.name.lower():
                raise ValidationError({'name': f'Название содержит запрещённое слово: {bad_word}'})
            if bad_word.lower() in self.description.lower():
                raise ValidationError({'description': f'Описание содержит запрещённое слово: {bad_word}'})
        if self.price < 0:
            raise ValidationError({'price': 'Цена не может быть отрицательной'})
