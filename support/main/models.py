from django.db import models


class User(models.Model):

    name = models.CharField('Имя', max_length=75)
    message = models.TextField('Сообщение')
    is_done = models.BooleanField('Решено', default=False)
    is_frozen = models.BooleanField('Заморожено', default=False)

    def __str__(self):
        return self.name


class Support(models.Model):

    name = models.CharField('Имя', max_length=75)
    user_name = models.CharField('Ответил пользователю', max_length=75)
    message = models.TextField('Ответ')

    def __str__(self):
        return self.name