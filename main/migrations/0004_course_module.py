# Generated by Django 5.1.4 on 2024-12-24 06:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_lesson_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Тақырыбы')),
                ('duration', models.PositiveSmallIntegerField(default=0, verbose_name='Ұзақтығы')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Бағасы')),
                ('ln', models.CharField(choices=[('ru', 'Русский'), ('kz', 'Қазақша')], max_length=128, verbose_name='Тілі')),
            ],
            options={
                'verbose_name': 'Цифрлық курс',
                'verbose_name_plural': 'Цифрлық курстар',
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Тақырыбы')),
                ('order', models.PositiveIntegerField(verbose_name='Order')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='main.course', verbose_name='Цифрлық курс')),
            ],
            options={
                'verbose_name': 'Модуль',
                'verbose_name_plural': 'Модульдер',
            },
        ),
    ]
