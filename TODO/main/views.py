from django.shortcuts import render
from datetime import datetime, timedelta

todos = [
    {
        'task': 'Task 1',
        'created': datetime.now(),
        'due_on': datetime.now() + timedelta(days=2),
        'owner': 'admin',
        'mark': False
    },
    {
        'task': 'Task 2',
        'created': datetime.now(),
        'due_on': datetime.now() + timedelta(days=2),
        'owner': 'admin',
        'mark': False
    },
    {
        'task': 'Task 3',
        'created': datetime.now(),
        'due_on': datetime.now() + timedelta(days=2),
        'owner': 'admin',
        'mark': False
    },
    {
        'task': 'Task 4',
        'created': datetime.now(),
        'due_on': datetime.now() + timedelta(days=2),
        'owner': 'admin',
        'mark': False
    },
    {
        'task': 'Task 0',
        'created': datetime.now(),
        'due_on': datetime.now() + timedelta(days=2),
        'owner': 'admin',
        'mark': True
    }
]


def todo(request):
    global todos
    context = {
        'todos': list(filter(lambda d: not d['mark'], todos)),
    }

    return render(request, 'todo_list.html', context=context)


def completed_todo(request, num):
    global todos
    context = {
        'todos': list(filter(lambda d: d['mark'], todos)),
    }

    return render(request, 'completed_todo_list.html', context=context)
