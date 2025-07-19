from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from catalog.models import Product


class ProductListView(ListView):
    """
    Представление для отображения списка всех опубликованных продуктов.
    """
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(DetailView):
    """
    Представление для отображения подробной информации о конкретном продукте.
    """
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'is_published']  # ← допиши остальные поля при необходимости
    success_url = reverse_lazy('catalog:product-list')

    def form_valid(self, form):
        """
        Устанавливает владельцем текущего пользователя при создании продукта.
        """
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Представление для редактирования продукта. Доступно только владельцу.
    """

    model = Product
    fields = ['name', 'is_published']  # ← допиши остальные поля при необходимости
    success_url = reverse_lazy('catalog:product-list')

    def test_func(self):
        """
        Проверяет, является ли текущий пользователь владельцем продукта.
        """
        product = self.get_object()
        return self.request.user == product.owner


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Представление для удаления продукта. Доступно владельцу или модератору.
    """
    model = Product
    success_url = reverse_lazy('catalog:product-list')

    def test_func(self):
        """
        Проверяет, является ли пользователь владельцем или входит в группу 'Модератор продуктов'.
        """
        product = self.get_object()
        user = self.request.user
        return user == product.owner or user.groups.filter(name='Модератор продуктов').exists()


class ProductUnpublishView(PermissionRequiredMixin, View):
    """
    Представление для снятия продукта с публикации.
    Требует права catalog.can_unpublish_product.
    """
    permission_required = 'catalog.can_unpublish_product'

    def post(self, request, pk):
        """
        Обрабатывает POST-запрос на снятие публикации с продукта.
        """
        product = get_object_or_404(Product, pk=pk)
        product.is_published = False
        product.save()
        return redirect('catalog:product-detail', pk=pk)
