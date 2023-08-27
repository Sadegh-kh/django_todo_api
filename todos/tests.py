from django.test import TestCase

from .models import Todo

# Create your tests here.


class TodoTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.todo = Todo.objects.create(title="test_do", description="do something")

    def test_todo_model(self):
        self.assertEqual(self.todo.title, "test_do")
        self.assertEqual(self.todo.date_do, None)
        self.assertEqual(self.todo.description, "do something")
        self.assertEqual(str(self.todo), "test_do")
