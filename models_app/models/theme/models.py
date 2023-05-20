# -*- coding: utf8 -*-
from django.db import models


class Theme(models.Model):
    name = models.CharField(max_length=255, verbose_name='Тематика')
    description = models.CharField(max_length=255, verbose_name='Описание')
    image = models.ImageField(upload_to="themes/", verbose_name="Картинка темы")
    rating = models.IntegerField(default=0, verbose_name="Посещаемость")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    category = models.ForeignKey(to='User', on_delete=models.CASCADE,
                                 related_name='categories', verbose_name='Категория')

    class Meta:
        db_table = 'themes'
        app_label = "models_app"
        verbose_name = 'Theme'
        verbose_name_plural = 'Themes'

    def __str__(self):
        return self.name