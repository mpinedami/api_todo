from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.todos.factories import TodoFactory
from apps.todos.models import Todo


class TodoModelTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.todo = TodoFactory.create()

    def test_model_content(self):
        todo = Todo.objects.first()
        self.assertEqual(self.todo.title, todo.title)
        self.assertEqual(self.todo.body, todo.body)
        self.assertEqual(self.todo, todo)

    def test_api_todo_list(self):
        url = reverse("todo_list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)

    def test_api_todo_detail(self):
        data = {"pk": self.todo.id}
        url = reverse("todo_detail", kwargs=data)
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo.title)
