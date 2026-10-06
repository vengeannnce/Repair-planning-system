"""Тесты класса Executor."""

from models import Executor
from models.executors import add_executor, find_executor_by_id


def test_executor_creation():
    executor = Executor(1, "Иван", "Электрик")
    assert executor.id == 1
    assert executor.name == "Иван"
    assert executor.specialization == "Электрик"


def test_executor_from_dict():
    data = {"id": 2, "name": "Петр", "specialization": "Плиточник"}
    executor = Executor.from_dict(data)
    assert executor.name == "Петр"


def test_add_and_find_executor():
    executors = []
    add_executor(executors, "Иван", "Электрик")
    assert find_executor_by_id(executors, 1) is executors[0]
    assert find_executor_by_id(executors, 99) is None