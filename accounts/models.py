from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(
        _('Қолданушы суреті'), upload_to='accounts/avatars/', null=True, blank=True,
        help_text=_('Сурет шаршы форматта болуы керек. Мысалы: (512x512)px')
    )
    profession = models.CharField(_('Профессия'), max_length=128, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _('Пайдаланушы')
        verbose_name_plural = _('Пайдаланушылар')
