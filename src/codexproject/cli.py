"""Command-line interface for codexproject."""

from __future__ import annotations

import argparse

from .project import Project


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage a tiny project task list")
    parser.add_argument("name", help="project name")
    parser.add_argument("--add", metavar="TASK", help="task text to add")
    parser.add_argument(
        "--complete",
        metavar="INDEX",
        type=int,
        help="zero-based index of the task to complete",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    project = Project(args.name)

    if args.add:
        project.add_task(args.add)
        print(f"Added task to {project.name}: {args.add}")

    if args.complete is not None:
        try:
            completed = project.complete_task(args.complete)
            print(f"Completed task: {completed}")
        except IndexError as error:
            parser.error(str(error))

    if not args.add and args.complete is None:
        print(f"Project '{project.name}' is ready. Add tasks with --add.")


if __name__ == "__main__":
    main()
