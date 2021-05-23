import datetime

from django.db import models


class TaskCategory(models.Model):
    category_name = models.CharField(verbose_name='Наименование категории', max_length=50, default="Категория",
                                     blank=True)

    class Meta:
        verbose_name = 'Категория задач'
        verbose_name_plural = 'Категории задач'


class Task(models.Model):
    task_name = models.CharField(verbose_name='Наименование задачи', max_length=200, default="Задача")
    bot_user = models.ForeignKey('bot_user.BotUser', verbose_name='Пользователь бота', on_delete=models.RESTRICT,
                                 default=True)
    category = models.ForeignKey('TaskCategory', verbose_name='Категория',
                                 on_delete=models.CASCADE, blank=True, null=True, related_name='task')
    countable_value = models.PositiveIntegerField(verbose_name='Исчисляемое значение', null=True, blank=True)
    date = models.DateField(verbose_name='Задачи на дату', default=datetime.date.today)
    done = models.BooleanField(verbose_name='Выполнено', default=None,
                               blank=True, null=True)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.task_name
