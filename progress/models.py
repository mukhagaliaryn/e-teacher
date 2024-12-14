from django.db import models
from django.contrib.auth import get_user_model
from main.models import Subject, Lesson
from django.utils.translation import gettext_lazy as _
User = get_user_model()


class UserSubject(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name=_('Қолданушы'), related_name="user_subjects")
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE,
        verbose_name=_('Пән'), related_name="user_subjects"
    )
    total_percent = models.PositiveSmallIntegerField(_('Жалпы ұпай пайызы'), default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'subject')
        verbose_name = _('Қолданушының пәні')
        verbose_name_plural = _('Қолданушының пәндері')

    def __str__(self):
        return f"{self.user} - {self.subject.title}"


class UserLesson(models.Model):
    user_subject = models.ForeignKey(
        UserSubject, on_delete=models.CASCADE,
        verbose_name=_('Қолданушының пәні'), related_name="user_lessons")
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE,
        verbose_name=_('Сабақ'), related_name="user_lessons"
    )
    lesson_score = models.DecimalField(_('Сабақтың баллы'), max_digits=5, decimal_places=2, blank=True, null=True)
    completed = models.BooleanField(_('Орындалды'), default=False)
    completed_at = models.DateTimeField(_('Орындалған уақыты'), blank=True, null=True)

    class Meta:
        unique_together = ('user_subject', 'lesson')
        verbose_name = _('Қолданушының сабағы')
        verbose_name_plural = _('Қолданушылардың сабағы')

    def __str__(self):
        return f"{self.user_subject.user} - {self.lesson.title} - {'Орындалды' if self.completed else 'Процессте'}"
