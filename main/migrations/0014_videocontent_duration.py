# Generated by Django 5.1.4 on 2024-12-14 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_videocontent_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='videocontent',
            name='duration',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Видео уақыт'),
        ),
    ]