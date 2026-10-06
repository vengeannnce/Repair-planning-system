"""Класс Task и функции обработки коллекции задач."""

from .executors import Executor
from .repairs import Repair

VALID_STATUSES = ("Не начато", "В работе", "Готово")


class Task:
    """Задача ремонта, связанная с объектом и исполнителем."""

    def __init__(
        self,
        task_id: int,
        name: str,
        repair: Repair,
        executor: Executor,
        status: str = "Не начато",
    ) -> None:
        """Создать задачу со ссылками на Repair и Executor."""
        self.id = task_id
        self.name = name
        self.repair = repair
        self.executor = executor
        if self.validate_status(status):
            self.status = status
        else:
            self.status = "Не начато"

    @staticmethod
    def validate_status(status: str) -> bool:
        """Проверить, что статус допустим."""
        return status in VALID_STATUSES

    @property
    def is_completed(self) -> bool:
        """Вернуть True, если задача завершена."""
        return self.status == "Готово"

    def start(self) -> None:
        """Перевести задачу в статус 'В работе'."""
        self.status = "В работе"

    def complete(self) -> None:
        """Перевести задачу в статус 'Готово'."""
        self.status = "Готово"

    def update_status(self, is_completed: bool) -> None:
        """Изменить статус задачи (совместимость с ПР2)."""
        if is_completed:
            self.complete()
        else:
            self.start()

    def to_dict(self) -> dict:
        """Вернуть данные задачи для JSON (связи через id)."""
        return {
            "id": self.id,
            "name": self.name,
            "repair_id": self.repair.id,
            "executor_id": self.executor.id,
            "status": self.status,
        }

    def __str__(self) -> str:
        """Строковое представление задачи."""
        return (
            f"ID: {self.id} | Задача: {self.name} | "
            f"Исполнитель: {self.executor.name} | "
            f"Объект: {self.repair.object_name} | "
            f"Статус: {self.status}"
        )


def assign_task(
    tasks: list[Task],
    task_name: str,
    repair: Repair,
    executor: Executor,
) -> Task:
    """Создать задачу и добавить её в коллекцию."""
    new_id = max([t.id for t in tasks], default=0) + 1
    task = Task(new_id, task_name, repair, executor)
    tasks.append(task)
    return task


def find_task_by_id(
    tasks: list[Task],
    task_id: int,
) -> Task | None:
    """Найти задачу по идентификатору."""
    for task in tasks:
        if task.id == task_id:
            return task
    return None


def update_task_status(
    tasks: list[Task],
    task_id: int,
    is_completed: bool,
) -> str:
    """Найти задачу и изменить её статус через метод объекта."""
    task = find_task_by_id(tasks, task_id)
    if task is None:
        return "Ошибка: задача не найдена."
    task.update_status(is_completed)
    return f"Статус задачи '{task.name}': [{task.status}]"


def filter_tasks_by_status(
    tasks: list[Task],
    status: str,
) -> list[Task]:
    """Отфильтровать задачи по статусу."""
    return [t for t in tasks if t.status == status]


def get_repair_summary(
    repairs: list[Repair],
    tasks: list[Task],
) -> str:
    """Сводка общего состояния ремонтов."""
    total_repairs = len(repairs)
    active_repairs = sum(1 for r in repairs if r.is_active)
    total_tasks = len(tasks)
    done_tasks = sum(1 for t in tasks if t.is_completed)
    remaining = total_tasks - done_tasks
    working = sorted(
        {t.executor.name for t in tasks if t.status == "В работе"}
    )
    workers = ", ".join(working) if working else "никто"
    return (
        f"Объектов: {total_repairs} (активных: {active_repairs}). "
        f"Задач: {total_tasks}, выполнено: {done_tasks}, "
        f"осталось: {remaining}. Сейчас работают: {workers}."
    )