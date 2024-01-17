from django.db import models

from config import settings
from users.models import NULLABLE


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    preview = models.ImageField(upload_to='course/', verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.title}{self.description}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    link_video = models.CharField(max_length=450, verbose_name='Ссылка на видео')
    preview = models.ImageField(upload_to='lesson/', verbose_name='Превью')

    def __str__(self):
        return f'{self.title}{self.description}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Payments(models.Model):
    payment_method = [
        ('cash', 'наличные'),
        ('transfer', 'перевод на счет')
    ]

    paid_course = [
        ('course', 'Курс'),
        ('lesson', 'Урок')
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Пользователь',null=True, blank=True)
    data_payments = models.DateField(verbose_name='Дата оплаты')
    paid_course = models.CharField(choices=paid_course, default='course', verbose_name='Что оплачено')
    payment_method = models.CharField(choices=payment_method, default='cash', verbose_name='Способ оплаты')

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Платежи'
        verbose_name_plural = 'Платежи'
