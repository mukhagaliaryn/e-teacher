from django.db import models
from django.utils.translation import gettext_lazy as _


# Genre model
class Genre(models.Model):
    name = models.CharField(_('Атауы'), max_length=255)
    slug = models.SlugField(_('Кілттік атауы'), max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Жанр')
        verbose_name_plural = _('Жанрлар')


# Author model
class Author(models.Model):
    first_name = models.CharField(_('Аты'), max_length=100)
    last_name = models.CharField(_('Тегі'), max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _('Автор')
        verbose_name_plural = _('Авторлар')


class Book(models.Model):
    title = models.CharField(_('Атауы'), max_length=255)
    poster = models.ImageField(_('Постер'), upload_to='books/posters/', blank=True, null=True)
    file = models.FileField(_('Файл'), upload_to='books/files/', blank=True, null=True)
    description = models.TextField(_('Анықтама'), blank=True)
    published_date = models.DateField(_('Шыққан уақыты'), null=True, blank=True)
    category = models.ForeignKey(
        Genre, on_delete=models.SET_NULL,
        null=True, related_name='books', verbose_name=_('Жанр'),
    )
    authors = models.ManyToManyField(Author, related_name='books', verbose_name=_('Авторлар'),)
    view = models.PositiveIntegerField(_('Қаралым'), default=0)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Кітап')
        verbose_name_plural = _('Кітаптар')
