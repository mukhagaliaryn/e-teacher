# Generated by Django 5.1.4 on 2024-12-14 10:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0007_lesson_subject'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_subjects', to='main.subject', verbose_name='Пән')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_subjects', to=settings.AUTH_USER_MODEL, verbose_name='Қолданушы')),
            ],
            options={
                'verbose_name': 'Қолданушының пәні',
                'verbose_name_plural': 'Қолданушының пәндері',
                'unique_together': {('user', 'subject')},
            },
        ),
    ]