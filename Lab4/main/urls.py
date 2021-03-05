from django.urls import path
from .views import todo, completed_todo

urlpatterns = [
    path('todos/', todo),
    path('todos/<int:list_id>/', todo),
    path('todos/<int:list_id>/completed/', completed_todo),
    path('todos/completed', completed_todo),
]