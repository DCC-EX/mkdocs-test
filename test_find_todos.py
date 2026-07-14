import unittest

import find_todos


class FindTodosTests(unittest.TestCase):
    def test_classify_todo_line(self):
        self.assertEqual(find_todos.classify_todo_line("This is ==TODO== item"), "normal")
        self.assertEqual(find_todos.classify_todo_line("This is ==TODO== LOW item"), "low")
        self.assertIsNone(find_todos.classify_todo_line("This has TODO without marker"))
        self.assertEqual(find_todos.classify_todo_line("This is ==todo== low"), "low")


if __name__ == "__main__":
    unittest.main()
