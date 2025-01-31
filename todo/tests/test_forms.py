from datetime import timedelta
from django.utils.timezone import now
from django.test import TestCase
from todo.forms import TaskForm


class TaskFormTest(TestCase):
    def test_valid_form(self):
        form = TaskForm(data={"content": "Test Task", "deadline": None, "tags": []})
        self.assertTrue(form.is_valid())

    def test_past_deadline(self):
        past_deadline = now() - timedelta(days=1)
        form = TaskForm(data={"content": "Test Task", "deadline": past_deadline})
        self.assertFalse(form.is_valid())
        self.assertIn("deadline", form.errors)

    def test_future_deadline(self):
        future_deadline = now() + timedelta(days=1)
        form = TaskForm(data={"content": "Test Task", "deadline": future_deadline})
        self.assertTrue(form.is_valid())
