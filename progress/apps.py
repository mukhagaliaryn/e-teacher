from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProgressConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'progress'
    verbose_name = _('Статистика қосымшасы')
