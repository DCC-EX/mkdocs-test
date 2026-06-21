from __future__ import annotations

import argparse
import os
import re
from pathlib import Path

TODO_PATTERN = re.compile(r"\bTODO\b", re.IGNORECASE)
EXCLUDE_LINE_PATTERN = re.compile(r"\bto-do/task list\b|/todo-report\.md|todo-report\.md\b", re.IGNORECASE)
DEFAULT_IGNORE_DIRS = {
    ".git",
}
DEFAULT_IGNORE_FILES = {
    ".DS_Store",
    "todo_report.md",
    "todo-report.md",
    "find_todos.py",
    "toc.md",
}
DEFAULT_IGNORE_SUFFIXES = {
    ".py",
    ".pyc",
    ".yml",
}


def is_ignored(path: Path) -> bool:
    # Ignore exact files by name
    if path.name in DEFAULT_IGNORE_FILES:
        return True
    # Ignore exact suffixes
    if path.suffix.lower() in DEFAULT_IGNORE_SUFFIXES:
        return True
    # Ignore any path segment that matches the configured directories
    if any(part in DEFAULT_IGNORE_DIRS for part in path.parts):
        return True
    return False


def iter_text_files(scan_root: Path):
    if not scan_root.exists():
        return

    for path in scan_root.rglob("*"):
        if is_ignored(path):
            continue
        if not path.is_file():
            continue
        try:
            raw = path.read_bytes()
        except OSError:
            continue
        if b"\x00" in raw:
            continue
        yield path


def build_report(root: Path, output_path: Path) -> int:
    output_path = output_path.resolve()
    scan_root = root / "docs"
    matches = []
    for path in iter_text_files(scan_root):
        if path.resolve() == output_path:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue

        for line_number, line in enumerate(text.splitlines(), start=1):
            if TODO_PATTERN.search(line) and not EXCLUDE_LINE_PATTERN.search(line):
                rel_path = path.relative_to(root).as_posix()
                link_path = os.path.relpath(path, output_path.parent).replace(os.sep, "/")
                matches.append(
                    {
                        "file": rel_path,
                        "line_number": line_number,
                        "line": line.strip(),
                        "link_path": link_path,
                    }
                )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        "# TODO Report\n\n"
        f"Scanned docs root: `{scan_root}`\n\n"
        f"Total TODO matches: {len(matches)}\n\n"
        + (
            "| File | Line | Line text |\n"
            "| --- | ---: | --- |\n"
            + "\n".join(
                f"| [{item['file']}]({item['link_path']}) | {item['line_number']} | {item['line']} |"
                for item in matches
            )
            + "\n"
        )
        if matches
        else "No TODO entries found.\n",
        encoding="utf-8",
    )
    return len(matches)


def on_post_build(config, **kwargs) -> None:
    root = Path(config["config_file_path"]).resolve().parent
    docs_dir = Path(config["docs_dir"]).resolve()
    output_path = docs_dir / "contributing" / "todo-report.md"
    count = build_report(root, output_path)
    print(f"TODO scan completed: {count} entries found.")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scan repository files for TODO markers and generate a markdown report."
    )
    parser.add_argument(
        "--root",
        default=".",
        help="Root directory to scan (default: current working directory).",
    )
    parser.add_argument(
        "--output",
        default="docs/contributing/todo-report.md",
        help="Output markdown file (default: docs/contributing/todo-report.md).",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = root / output_path

    count = build_report(root, output_path)
    print(f"Found {count} TODO entries.")
    print(f"Report written to: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
