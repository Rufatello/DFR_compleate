from django.db import models

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
