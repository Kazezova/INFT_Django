from django.db import models
from django.utils import timezone
from auth_.models import MainUser


class TodoList(models.Model):
    owner = models.ForeignKey(MainUser, on_delete=models.CASCADE, verbose_name='Владелец', default=1)
    title = models.CharField(max_length=255, verbose_name='Название листа: ', null=True, blank=True)

    class Meta:
        verbose_name = 'Список'
        verbose_name_plural = 'Списки'

    def __str__(self):
        return self.title


class Task(models.Model):
    list = models.ForeignKey(TodoList, on_delete=models.CASCADE, verbose_name='Список')
    title = models.CharField(max_length=255, null=True, blank=True, verbose_name='Задача')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    due_on = models.DateTimeField(blank=True, null=True, verbose_name='Дедлайн до')
    mark = models.BooleanField(default=False, null=False, blank=False, verbose_name='Отметка')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['-created']

    def __str__(self):
        return self.title
