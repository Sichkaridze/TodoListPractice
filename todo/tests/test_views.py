from django.test import TestCase
from todo.models import Task, Tag


class TaskViewTest(TestCase):
    def test_task_list_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_task_complete(self):
        task = Task.objects.create(content="Task")
        self.client.post(f'/task/{task.pk}/complete/')
        task.refresh_from_db()
        self.assertTrue(task.is_done)

    def test_task_undo(self):
        task = Task.objects.create(content="Task")
        self.client.post(f'/task/{task.pk}/undo/')
        task.refresh_from_db()
        self.assertFalse(task.is_done)
