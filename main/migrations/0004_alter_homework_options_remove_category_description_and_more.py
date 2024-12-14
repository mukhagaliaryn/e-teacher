# Generated by Django 5.1.4 on 2024-12-14 07:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_comment_author_alter_comment_lesson'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homework',
            options={'verbose_name': 'Үй жұмысы', 'verbose_name_plural': 'Үй жұмыстары'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.AddField(
            model_name='lesson',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Анықтамасы'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='order',
            field=models.PositiveIntegerField(verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='order',
            field=models.PositiveIntegerField(verbose_name='Order'),
        ),
        migrations.CreateModel(
            name='FrameContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='URL сілтеме')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frame_contents', to='main.lesson', verbose_name='Сабақ')),
            ],
            options={
                'verbose_name': 'Фрейм контент',
                'verbose_name_plural': 'Фрейм контенттер',
            },
        ),
    ]
