# Generated by Django 4.0 on 2023-07-19 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models_app', '0004_theme_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='popular_image',
            field=models.ImageField(default=1, upload_to='themes/', verbose_name='Картинка темы для популярных'),
            preserve_default=False,
        ),
    ]
