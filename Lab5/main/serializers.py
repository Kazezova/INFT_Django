from rest_framework import serializers
from main.models import TodoList, Task
from auth_.serializers import MainUserSerializer


class TodoListSerializer(serializers.ModelSerializer):
    owner = MainUserSerializer()

    class Meta:
        model = TodoList
        fields = ('id', 'title', 'owner')


class TaskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'title', 'mark',)


class TaskDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'title', 'created', 'due_on', 'mark')
