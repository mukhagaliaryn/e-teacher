# Generated by Django 5.1.4 on 2024-12-19 13:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Аты')),
                ('last_name', models.CharField(max_length=100, verbose_name='Тегі')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторлар',
            },
        ),
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
                ('poster', models.ImageField(blank=True, null=True, upload_to='books/posters/', verbose_name='Постер')),
                ('file', models.FileField(blank=True, null=True, upload_to='books/files/', verbose_name='Файл')),
                ('description', models.TextField(blank=True, verbose_name='Анықтама')),
                ('published_date', models.DateField(blank=True, null=True, verbose_name='Шыққан уақыты')),
                ('view', models.PositiveIntegerField(default=0, verbose_name='Қаралым')),
                ('authors', models.ManyToManyField(related_name='books', to='books.author', verbose_name='Авторлар')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to='books.genre', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Кітап',
                'verbose_name_plural': 'Кітаптар',
            },
        ),
    ]
