from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, max_length=150, verbose_name='Почта')
    phone = models.IntegerField(verbose_name='Телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='user/', verbose_name='Аватар', **NULLABLE)
    city = models.CharField(max_length=150, verbose_name='Город', **NULLABLE)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

