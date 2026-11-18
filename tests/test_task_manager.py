import unittest
from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task("Read chapter 1")
        #self.assertEqual(task["title"], "Read chapter 1")
        self.assertEqual(task["title"], "Wrong Title")
        self.assertFalse(task["completed"])
        self.assertEqual(len(self.manager.get_tasks()), 1)

    def test_complete_task(self):
        task = self.manager.add_task("Prepare presentation")
        self.assertTrue(self.manager.complete_task(task["id"]))
        self.assertTrue(self.manager.get_tasks()[0]["completed"])

    def test_delete_task(self):
        task = self.manager.add_task("Submit assignment")
        self.assertTrue(self.manager.delete_task(task["id"]))
        self.assertEqual(len(self.manager.get_tasks()), 0)

    def test_reject_empty_title(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("   ")

    def test_invalid_task_id(self):
        self.assertFalse(self.manager.complete_task(999))
        self.assertFalse(self.manager.delete_task("abc"))

if __name__ == "__main__":
    unittest.main()
