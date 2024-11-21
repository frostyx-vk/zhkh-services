from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

class ProfilePortal(models.Model):
    class TypeProperty(models.TextChoices):
        HABITABLE = 'HABITABLE', 'Жилое'
        NOT_RESIDENTIAL = 'NOT_RESIDENTIAL', 'Не жилое'
        PARKING = 'PARKING', 'Парковочное место'

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    number_ls = models.PositiveIntegerField(verbose_name='Номер лицевого счета', blank=True)
    address = models.CharField(verbose_name='Адрес', max_length=255, blank=True)
    square = models.PositiveIntegerField(verbose_name='Площадь', blank=True)
    type = models.CharField(choices=TypeProperty.choices, default=TypeProperty.HABITABLE, max_length=255, blank=True)

    class Meta:
        verbose_name = 'Профиль портала'
        verbose_name_plural = 'Профили портала'

    def __str__(self):
        return self.user.username