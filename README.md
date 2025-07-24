# 🐍 My Django Project

## 📋 Описание

Учебный проект на Django с реализацией:

- приложения `catalog` для управления товарами,
- приложения `blogs` для публикации блоговых записей,
- домашней страницы и страницы "Контакты",
- системы прав доступа и групп пользователей.

Проект организован по структуре GitFlow:

- `main` — продуктивная версия (релизы),
- `develop` — основная ветка разработки,
- `feature/*` — ветки для разработки новых функций (например, `feature/homework-1`).

## 🔐 Права доступа

В проекте реализована система разграничения прав доступа с использованием:

- Django-групп (`Group`),
- стандартных и кастомных разрешений (`Permission`),
- миксинов:
  - `LoginRequiredMixin`
  - `UserPassesTestMixin`
  - `PermissionRequiredMixin`

### 🛡 Группа "Модератор продуктов"

Для модерации товаров создаётся специальная группа "Модератор продуктов" с правами:

- `can_unpublish_product` — может снимать товары с публикации,
- `delete_product` — может удалять товары.

## 🧑‍💻 Пользовательские разрешения

В модели Product добавлено собственное разрешение:
class Meta:
    permissions = [
("can_unpublish_product", "Can unpublish product"),
]

## 👮 Контроль доступа в представлениях

Права контролируются с помощью CBV (Class-Based Views) и миксинов.

Пример проверки принадлежности к группе:
def test_func(self):
    return self.request.user.groups.filter(name='Модератор продуктов').exists()
    
Пример проверки пользовательского разрешения:
def test_func(self):
    return self.request.user.has_perm('catalog.can_unpublish_product')

## ⚙️ Установка и запуск
1- Клонируй проект: git clone https://github.com/Fish3r228/django.git
cd django
2- Создай и активируй виртуальное окружение:
python -m venv venv
source venv/bin/activate  # для Linux/macOS
.\venv\Scripts\activate   # для Windows
3- Установи зависимости:
pip install -r requirements.txt
4- Применить миграции и создать суперпользователя:
python manage.py migrate
python manage.py createsuperuser
5- Запусти сервер: 
python manage.py runserver




