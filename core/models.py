from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models as geomodels
from django.db import models


class User(AbstractUser):
    patronymic = models.CharField('отчество', max_length=255, blank=True)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ['id']

    def __str__(self) -> str:
        return self.fullname or self.username

    def fullname(self) -> str:
        return ' '.join(filter(bool, [self.last_name, self.first_name, self.patronymic]))


class Field(geomodels.Model):
    name = models.CharField(max_length=100, verbose_name='Название поля')
    location_x = models.FloatField(verbose_name='Координата X')
    location_y = models.FloatField(verbose_name='Координата Y')
    area = models.FloatField(verbose_name='Площадь')

    class Meta:
        verbose_name = 'Поле'
        verbose_name_plural = 'Поля'

    def __str__(self) -> str:
        return str(self.name)
