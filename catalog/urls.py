from django.urls import path
from .views import ProductListView, ProductDetailView, ContactsView

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
]
