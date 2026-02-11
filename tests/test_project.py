from codexproject import Project


def test_add_task_strips_whitespace() -> None:
    project = Project("demo")

    project.add_task("  write docs  ")

    assert project.tasks == ["write docs"]


def test_add_task_rejects_empty_input() -> None:
    project = Project("demo")

    try:
        project.add_task("   ")
    except ValueError as error:
        assert str(error) == "task cannot be empty"
    else:
        raise AssertionError("Expected ValueError")


def test_complete_task_removes_item() -> None:
    project = Project("demo", tasks=["a", "b"])

    completed = project.complete_task(0)

    assert completed == "a"
    assert project.tasks == ["b"]
