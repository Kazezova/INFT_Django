from django.urls import path, include
from main.views import TodoListViewSet, TaskListViewSet, TaskDetailViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('todos/todolist', TodoListViewSet, basename='main')
router.register('todos/tasklist', TaskListViewSet, basename='main')
router.register('todos/detail', TaskDetailViewSet, basename='main')
task_detail = TaskDetailViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
})
urlpatterns = [
    path('todos/tasklist/<int:pk>/completed', TaskListViewSet.as_view({'get': 'get_completed', })),
    path('todos/detail/<int:pk>', task_detail)
]
urlpatterns += router.urls
