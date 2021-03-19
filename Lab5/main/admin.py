from django.contrib import admin
from main.models import Task, TodoList
# Register your models here.
admin.site.register(Task)
admin.site.register(TodoList)