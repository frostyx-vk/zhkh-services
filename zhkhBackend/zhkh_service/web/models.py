from django.db import models


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