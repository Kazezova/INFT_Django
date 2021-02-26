from django.urls import path
from .views import todo, completed_todo

urlpatterns = [
    path('todos/', todo),
    path('todos/<int:num>/completed/', completed_todo)
]