"""Тесты класса Task: композиция, статусы, функции коллекции."""

from models import Executor, Repair, Task
from models.tasks import (
    assign_task,
    filter_tasks_by_status,
    get_repair_summary,
    update_task_status,
)


def make_objects():
    """Создать связанные объекты для тестов."""
    repair = Repair(1, "Кухня", 15.5)
    executor = Executor(1, "Иван", "Электрик")
    return repair, executor


def test_task_composition():
    repair, executor = make_objects()
    task = Task(1, "Проводка", repair, executor)
    assert task.repair is repair
    assert task.executor is executor
    assert task.status == "Не начато"
    assert not task.is_completed


def test_task_status_change():
    repair, executor = make_objects()
    task = Task(1, "Проводка", repair, executor)
    task.start()
    assert task.status == "В работе"
    task.complete()
    assert task.is_completed


def test_update_task_status_function():
    repair, executor = make_objects()
    tasks = []
    assign_task(tasks, "Плитка", repair, executor)
    update_task_status(tasks, 1, True)
    assert tasks[0].status == "Готово"


def test_filter_and_summary():
    repair, executor = make_objects()
    tasks = [
        Task(1, "Проводка", repair, executor, "Готово"),
        Task(2, "Плитка", repair, executor, "В работе"),
    ]
    assert len(filter_tasks_by_status(tasks, "Готово")) == 1
    summary = get_repair_summary([repair], tasks)
    assert "выполнено: 1" in summary
    assert "Иван" in summary