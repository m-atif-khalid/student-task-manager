
import unittest
from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task("Study Python")
        self.assertEqual(task["title"], "Study Python")

    def test_complete_task(self):
        task = self.manager.add_task("Complete assignment")
        self.assertTrue(self.manager.complete_task(task["id"]))
        self.assertTrue(self.manager.get_tasks()[0]["completed"])

    def test_delete_task(self):
        task = self.manager.add_task("Read book")
        self.assertTrue(self.manager.delete_task(task["id"]))
        self.assertEqual(len(self.manager.get_tasks()), 0)

    def test_empty_task(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("")

if __name__ == "__main__":
    unittest.main()
