# -*- coding: utf8 -*-
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        db_table = 'categories'
        app_label = "models_app"
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
