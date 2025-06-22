# blog/models.py
from django.db import models
from django.urls import reverse

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # дата создания
    updated_at = models.DateTimeField(auto_now=True)      # дата изменения

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Возвращает ссылку на страницу с деталями записи блога
        return reverse('blog_detail', kwargs={'pk': self.pk})
