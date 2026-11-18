import unittest
from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task_success(self):
        """Test adding a task with a valid non-empty title."""
        task = self.manager.add_task("Review Chapter 4 DevOps")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Review Chapter 4 DevOps")
        self.assertFalse(task.completed)
        self.assertEqual(len(self.manager.get_all_tasks()), 1)

    def test_add_task_validation_failure(self):
        """Test that empty or whitespace titles raise ValueError."""
        with self.assertRaises(ValueError):
            self.manager.add_task("")
        with self.assertRaises(ValueError):
            self.manager.add_task("   ")

    def test_complete_task_success(self):
        """Test marking an existing task as completed."""
        task = self.manager.add_task("Prepare Lecture Slides")
        result = self.manager.complete_task(task.id)
        self.assertTrue(result)
        self.assertTrue(task.completed)

    def test_complete_task_nonexistent_id(self):
        """Test marking a non-existent task raises KeyError."""
        with self.assertRaises(KeyError):
            self.manager.complete_task(999)

    def test_delete_task_success(self):
        """Test deleting a valid task by ID."""
        task = self.manager.add_task("Temporary Task Item")
        result = self.manager.delete_task(task.id)
        self.assertTrue(result)
        self.assertEqual(len(self.manager.get_all_tasks()), 0)

    def test_delete_task_nonexistent_id(self):
        """Test deleting a non-existent task raises KeyError."""
        with self.assertRaises(KeyError):
            self.manager.delete_task(999)


    def test_is_completed_helper(self):
        task = self.manager.add_task("Check status helper")
        self.assertFalse(self.manager.is_completed(task.id))
        self.manager.complete_task(task.id)
        self.assertTrue(self.manager.is_completed(task.id))

    def test_delete_decreases_task_count(self):
        t1 = self.manager.add_task("Task 1")
        t2 = self.manager.add_task("Task 2")
        self.assertEqual(self.manager.get_task_count(), 2)
        self.manager.delete_task(t1.id)
        self.assertEqual(self.manager.get_task_count(), 1)

if __name__ == "__main__":
    unittest.main()

    def test_deliberate_failure_for_ci_demo(self):
        """Demonstrates automated CI failure on broken code/test."""
        self.assertEqual(1, 2, "Deliberate failure to demonstrate CI pipeline catch")
