from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # Переопределяем email, делаем его уникальным
    email = models.EmailField(unique=True)

    # Поле аватара — загружаемое изображение
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    # Телефон — строка, необязательное поле
    phone = models.CharField(max_length=20, blank=True, null=True)

    # Страна — строка, необязательное поле
    country = models.CharField(max_length=50, blank=True, null=True)

    # Указываем, что поле email будет использоваться как имя пользователя
    USERNAME_FIELD = 'email'

    # Обязательное поле username (требуется AbstractUser)
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
