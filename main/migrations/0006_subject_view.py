# Generated by Django 5.1.4 on 2024-12-14 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_category_slug_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='view',
            field=models.PositiveIntegerField(default=0, verbose_name='Қаралым'),
        ),
    ]