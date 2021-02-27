from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class Project(models.Model):
    title = models.CharField('Название проекта', max_length=255)
    code = models.CharField('Код проекта', max_length=5)
    preview = models.ImageField('Превью', blank=True, null=True)
    deadline = models.DateTimeField('Дедлайн', blank=True, null=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Автор',
        related_name='projects'
    )

    def __str__(self):
        return self.code
