"""Загрузка и сохранение объектов предметной области в JSON."""

import json
import os

from models import Executor, Repair, Task
from models.executors import find_executor_by_id
from models.repairs import find_repair_by_id


def _load_json(filename: str) -> list[dict]:
    """Прочитать список словарей из JSON-файла."""
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError) as error:
        print(f"Ошибка чтения {filename}: {error}")
        return []


def _save_json(filename: str, data: list[dict]) -> None:
    """Записать список словарей в JSON-файл."""
    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except OSError as error:
        print(f"Ошибка записи {filename}: {error}")


def load_repairs(filename: str) -> list[Repair]:
    """Загрузить ремонты из JSON как объекты Repair."""
    return [Repair.from_dict(item) for item in _load_json(filename)]


def save_repairs(filename: str, repairs: list[Repair]) -> None:
    """Сохранить ремонты в JSON."""
    _save_json(filename, [r.to_dict() for r in repairs])


def load_executors(filename: str) -> list[Executor]:
    """Загрузить исполнителей из JSON как объекты Executor."""
    return [Executor.from_dict(item) for item in _load_json(filename)]


def save_executors(filename: str, executors: list[Executor]) -> None:
    """Сохранить исполнителей в JSON."""
    _save_json(filename, [e.to_dict() for e in executors])


def load_tasks(
    filename: str,
    repairs: list[Repair],
    executors: list[Executor],
) -> list[Task]:
    """Загрузить задачи, восстановив связи с Repair и Executor."""
    tasks = []
    for item in _load_json(filename):
        repair = find_repair_by_id(repairs, item["repair_id"])
        executor = find_executor_by_id(executors, item["executor_id"])
        if repair is None or executor is None:
            print(f"Задача {item.get('id')} не загружена: "
                  "не найден объект или исполнитель.")
            continue
        tasks.append(Task(
            task_id=item["id"],
            name=item["name"],
            repair=repair,
            executor=executor,
            status=item.get("status", "Не начато"),
        ))
    return tasks


def save_tasks(filename: str, tasks: list[Task]) -> None:
    """Сохранить задачи в JSON (связи через идентификаторы)."""
    _save_json(filename, [t.to_dict() for t in tasks])