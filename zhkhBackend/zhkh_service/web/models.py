from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models


def is_nan_validator(value):
    import math
    if math.isnan(value):
        raise ValidationError('Недопустимое значение поля. Поле не может быть NaN')


class News(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    description = models.TextField('Содержание')
    image = models.ImageField('Изображение', upload_to='images/news/', blank=True)
    date_created = models.DateTimeField('Дата добавления', auto_now_add=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-date_created']

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Содержание')
    price = models.FloatField('Цена', validators=[MinValueValidator(0), is_nan_validator])
    order = models.PositiveIntegerField('Порядок вывода', default=0)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['order']

    def __str__(self):
        return self.title