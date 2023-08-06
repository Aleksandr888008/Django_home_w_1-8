# -*- coding: utf-8 -*-
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    name = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    content_blog = models.TextField(verbose_name='Содержимое')
    image_blog = models.ImageField(upload_to='blog/', verbose_name='Изображение', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Признак публикации')
    views_count = models.IntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'