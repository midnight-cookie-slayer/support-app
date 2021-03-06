# Generated by Django 3.2.7 on 2021-10-05 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='Имя')),
                ('message', models.TextField(default='Нет сообщения', verbose_name='Сообщение')),
                ('is_support', models.BooleanField(default=False, verbose_name='Сапорт?')),
                ('is_done', models.BooleanField(default=False, verbose_name='Решено?')),
                ('is_frozen', models.BooleanField(default=False, verbose_name='Заморожено?')),
            ],
        ),
    ]
