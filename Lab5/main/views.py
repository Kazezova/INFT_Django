from django.shortcuts import render, get_object_or_404
from rest_framework import generics, mixins, viewsets, status
from main.models import TodoList, Task
from main.serializers import TaskDetailSerializer, TodoListSerializer, TaskListSerializer
from auth_.models import MainUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action


class TodoListViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TodoListSerializer

    def get_queryset(self):
        queryset = TodoList.objects.all()
        return queryset

    def list(self, request):
        user = request.user
        queryset = self.get_queryset().filter(owner__pk=user.pk)
        serializer = TodoListSerializer(queryset, many=True)
        return Response(serializer.data)


class TaskListViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskListSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
        return queryset

    def check_user(self, request, pk):
        user = request.user
        users_todos = TodoList.objects.filter(owner__pk=user.pk)
        todos = [users_todos[i].pk for i in range(len(users_todos))]
        return int(pk) in todos

    def retrieve(self, request, pk=None):
        if self.check_user(request, pk):
            queryset = self.get_queryset().filter(list__pk=pk)
            serializer = TaskListSerializer(queryset, many=True)
            return Response(serializer.data)
        return Response({'error': 'У вас нет такого листа.'}, status=status.HTTP_404_NOT_FOUND)

    def get_completed(self, request, pk=None):
        if self.check_user(request, pk):
            queryset = self.get_queryset().filter(list__pk=pk, mark=True)
            serializer = TaskListSerializer(queryset, many=True)
            return Response(serializer.data)
        return Response({'error': 'У вас нет такого листа.'}, status=status.HTTP_404_NOT_FOUND)


class TaskDetailViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskDetailSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
        return queryset

    def check_user(self, request, pk):
        user = request.user
        users_todos = TodoList.objects.filter(owner__pk=user.pk)
        todos = [users_todos[i].pk for i in range(len(users_todos))]
        queryset = self.get_queryset()
        task = get_object_or_404(queryset, pk=pk)
        return task.list.pk in todos

    def retrieve(self, request, pk=None):
        if self.check_user(request, pk):
            task = get_object_or_404(self.get_queryset(), pk=pk)
            serializer = TaskDetailSerializer(task)
            return Response(serializer.data)
        return Response({'error': 'У вас нет такого таска.'}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        if self.check_user(request, pk):
            # print(request.data['title'])
            task = get_object_or_404(self.get_queryset(), pk=pk)
            task.title = request.data['title']
            task.due_on = request.data['due_on']
            task.mark = request.data['mark']
            task.save()
            serializer = TaskDetailSerializer(task)
            return Response(serializer.data)
        return Response({'error': 'У вас нет доступа к таску.'}, status=status.HTTP_404_NOT_FOUND)
