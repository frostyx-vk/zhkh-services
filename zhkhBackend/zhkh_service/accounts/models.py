from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Profile(models.Model):
    class Gender(models.TextChoices):
        MALE = 'MALE', 'Мужской'
        FEMALE = 'FEMALE', 'Женский'
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    first_name = models.CharField('Имя', max_length=30)
    middle_name = models.CharField('Отчество', max_length=150)
    last_name = models.CharField('Фамилия', max_length=150)
    gender = models.CharField('Пол', choices=Gender.choices, max_length=6)
    birth_date = models.DateField('Дата рождения')
    email = models.EmailField('Email адрес')
    phone = models.CharField(verbose_name='Телефон', unique=True, max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return self.get_full_name() if self.get_full_name() else self.user.__str__() if hasattr(self, 'user') else 'No name'

    def get_full_name(self):
        return  ' '.join(filter(None, [self.last_name, self.first_name, self.middle_name]))


class PortalUser(Profile):
    series = models.PositiveIntegerField('Серия', blank=True)
    number = models.PositiveIntegerField('Номер', blank=True)
    issued = models.CharField('Выдан', max_length=255, blank=True)
    departament_code = models.PositiveIntegerField('Код подразделения', blank=True)
    date_issue = models.DateField('Дата выдачи', blank=True)

    class Meta:
        verbose_name = 'Пользователь портала'
        verbose_name_plural = 'Пользователи портала'

