# blog/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import BlogPost

class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'  # Можно указать свой шаблон
    context_object_name = 'posts'

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'

class BlogCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'content']  # Заменить на поля вашей модели
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog_list')

class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'content']
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog_list')

class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog_list')
