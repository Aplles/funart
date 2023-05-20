# -*- coding: utf8 -*-
from django.db import models


class Coloring(models.Model):
    VERTICAL = 'VERTICAL'
    HORIZONTAL = 'HORIZONTAL'
    SQUARE = 'SQUARE'

    TYPES = (
        (VERTICAL, 'Вертикальное'),
        (HORIZONTAL, 'Горизонтальное'),
        (SQUARE, 'Квадратное'),
    )

    name = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='colorings/', verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    type = models.CharField(max_length=10, choices=TYPES, verbose_name='Тип', default=HORIZONTAL)
    theme = models.ForeignKey(to='Theme', on_delete=models.CASCADE,
                                 related_name='themes', verbose_name='Тематика')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'colorings'
        app_label = "models_app"
        verbose_name = 'Coloring'
        verbose_name_plural = 'Colorings'
