from django.db import models


class User(models.Model):

    name = models.CharField('Имя', max_length = 75)
    message = models.TextField('Сообщение', default='Нет сообщения')
    is_support = models.BooleanField('Сапорт?', default=False)
    is_done = models.BooleanField('Решено?', default=False)
    is_frozen = models.BooleanField('Заморожено?', default=False)

    def __str__(self):
        return self.name