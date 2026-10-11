import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

import find_todos


class FindTodosTests(unittest.TestCase):
    def test_classify_todo_line(self):
        self.assertEqual(find_todos.classify_todo_line("This is ==TODO== item"), "normal")
        self.assertEqual(find_todos.classify_todo_line("This is ==TODO== LOW item"), "low")
        self.assertIsNone(find_todos.classify_todo_line("This has TODO without marker"))
        self.assertEqual(find_todos.classify_todo_line("This is ==todo== low"), "low")

    def test_build_report_scans_snippets_without_linking_them(self):
        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            docs_file = root / "docs" / "guide.md"
            snippets_file = root / "snippets" / "example.md"
            output_path = root / "docs" / "contributing" / "todo-report.md"
            docs_file.parent.mkdir(parents=True)
            snippets_file.parent.mkdir(parents=True)
            docs_file.write_text("Docs ==TODO== item\n", encoding="utf-8")
            snippets_file.write_text("Snippet ==TODO== item\n", encoding="utf-8")

            count = find_todos.build_report(root, output_path)
            report = output_path.read_text(encoding="utf-8")

        self.assertEqual(count, 2)
        self.assertIn("[docs/guide.md](", report)
        self.assertIn("| snippets/example.md |", report)
        self.assertNotIn("[snippets/example.md](", report)


if __name__ == "__main__":
    unittest.main()
