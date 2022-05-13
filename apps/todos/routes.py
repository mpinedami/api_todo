from django.urls import path
from rest_framework.routers import SimpleRouter

from .viewsets import DetailTodo, ListTodo

router = SimpleRouter()

urlpatterns = [
    path("", ListTodo.as_view(), name="todo_list"),
    path("<int:pk>/", DetailTodo.as_view(), name="todo_detail"),
]
