from django.contrib.auth.models import AbstractUser
from django.db import models


# Базовый класс User переопределяется, для добавления новых атрибутов
class MetroUser(AbstractUser):
    """
    Класс MetroUser представляет пользователя в системе метро.

    Атрибуты:
    email (EmailField): Электронная почта пользователя, уникальная для каждого пользователя.
    full_name (CharField): Полное имя пользователя (ФИО), максимальная длина - 100 символов.
    avatar (ImageField): Фотография пользователя, загружается в директорию 'avatars/'.
                         Может быть пустым или отсутствовать (null=True, default=None).
    address (CharField): Адрес пользователя, максимальная длина - 100 символов.
    """

    email = models.EmailField(verbose_name='почта', unique=True)
    full_name = models.CharField(verbose_name='ФИО', max_length=100)
    avatar = models.ImageField(
        verbose_name='фото',
        upload_to='avatars/',
        null=True,
        blank=True,
        default=None,
    )
    address = models.CharField(verbose_name='адрес', max_length=100)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
