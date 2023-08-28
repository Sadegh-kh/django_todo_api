from urllib import response

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Todo

# Create your tests here.


class TodoTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.todo = Todo.objects.create(title="test_do", description="do something")

    def test_todo_model(self):
        self.assertEqual(self.todo.title, "test_do")
        self.assertEqual(self.todo.date_do, None)
        self.assertEqual(self.todo.description, "do something")
        self.assertEqual(str(self.todo), "test_do")

    def test_list_todo_api(self):
        response = self.client.get(reverse("todos_api:todo_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.todo)

    def test_detail_todo_api(self):
        response = self.client.get(
            reverse("todos_api:todo_detail", kwargs={"pk": self.todo.id}),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.todo)
