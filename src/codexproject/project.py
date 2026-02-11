"""Core domain model for the starter project."""

from dataclasses import dataclass, field


@dataclass(slots=True)
class Project:
    """A tiny in-memory project model that manages tasks."""

    name: str
    tasks: list[str] = field(default_factory=list)

    def add_task(self, task: str) -> None:
        """Add a non-empty task to the project."""
        cleaned = task.strip()
        if not cleaned:
            raise ValueError("task cannot be empty")
        self.tasks.append(cleaned)

    def complete_task(self, index: int) -> str:
        """Remove and return a task by index."""
        if index < 0 or index >= len(self.tasks):
            raise IndexError("task index out of range")
        return self.tasks.pop(index)
