# Generated by Django 5.1.4 on 2024-12-18 05:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Атауы')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Кілттік атауы')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанрлар',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Атауы')),
                ('description', models.TextField(blank=True, verbose_name='Анықтама')),
                ('published_date', models.DateField(blank=True, null=True, verbose_name='Шыққан уақыты')),
                ('authors', models.ManyToManyField(related_name='books', to=settings.AUTH_USER_MODEL, verbose_name='Авторлар')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to='books.genre', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Кітап',
                'verbose_name_plural': 'Кітаптар',
            },
        ),
    ]
