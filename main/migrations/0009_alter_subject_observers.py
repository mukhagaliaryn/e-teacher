# Generated by Django 5.1.4 on 2024-12-14 12:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_subject_observers'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='observers',
            field=models.ManyToManyField(blank=True, related_name='access_subjects', to=settings.AUTH_USER_MODEL, verbose_name='Жазылушылар'),
        ),
    ]
