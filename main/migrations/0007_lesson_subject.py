# Generated by Django 5.1.4 on 2024-12-14 09:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_subject_view'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='main.subject', verbose_name='Пәндер'),
        ),
    ]
