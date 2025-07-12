from django.urls import path
from catalog import views

urlpatterns = [
    path('category/<int:category_id>/', views.products_by_category, name='products_by_category'),
]
