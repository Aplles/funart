# Generated by Django 4.0 on 2023-11-11 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models_app', '0005_theme_popular_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
    ]
