from django.shortcuts import render
from main.models import TodoList, Task


def todo(request, list_id=''):
    if list_id:
        context = {
            'list': TodoList.objects.get(id=list_id),
            'todos': Task.objects.all().filter(list=list_id, mark=False)
        }
    else:
        context = {
            'list': 'All',
            'todos': Task.objects.all().filter(mark=False)
        }

    return render(request, 'todo_list.html', context=context)


def completed_todo(request, list_id=''):
    if list_id:
        context = {
            'list': TodoList.objects.get(id=list_id),
            'todos': Task.objects.all().filter(list=list_id, mark=True)
        }
    else:
        context = {
            'list': 'All',
            'todos': Task.objects.all().filter(mark=True)
        }

    return render(request, 'completed_todo_list.html', context=context)
