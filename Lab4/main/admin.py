from django.contrib import admin
from main.models import Task, TodoList


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['list', 'title', 'created', 'due_on', 'owner', 'mark', ]
    ordering = ['title']
    search_fields = ['title', 'list__title', ]
    list_filter = ['created', 'list__title', 'mark']


admin.site.register(TodoList)
