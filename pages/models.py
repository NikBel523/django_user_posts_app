from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

TITLE_MAX_LENGTH = 30


class Post(models.Model):
    """Модель для публикаций."""

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        verbose_name='Заголовок',
    )
    text = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации',
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('-created_at',)
        default_related_name = 'posts'

    def __str__(self) -> str:
        return self.title
