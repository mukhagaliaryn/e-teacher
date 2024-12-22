# Generated by Django 5.1.4 on 2024-12-22 11:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userhomework',
            name='user_lesson',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_homeworks', to='progress.userlesson', verbose_name='Үй жұмысы'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='homework',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Тапсырма мәтіні'),
        ),
        migrations.AlterField(
            model_name='userhomework',
            name='homework',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_homeworks', to='progress.homework', verbose_name='Үй жұмысы'),
        ),
    ]