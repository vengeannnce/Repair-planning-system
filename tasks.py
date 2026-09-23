def assign_task(tasks: list[dict], task_name: str, executor_name: str, repair_id: int) -> dict:
    """
    Функция из ПР1: Управление задачами.
    Создание задачи и назначение Исполнителя.
    """
    new_id = max([t["id"] for t in tasks], default=0) + 1
    task = {
        "id": new_id,
        "name": task_name,
        "executor": executor_name,
        "repair_id": repair_id,
        "status": "Не начато"
    }
    tasks.append(task)
    return task


def update_status(tasks: list[dict], task_id: int, is_completed: bool) -> str:
    """
    Функция из ПР1: Отслеживание прогресса.
    Простое переключение Статусов задач.
    """
    for task in tasks:
        if task["id"] == task_id:
            if is_completed:
                task["status"] = "Готово"
            else:
                task["status"] = "В работе"
            return f"Статус задачи '{task['name']}' изменен на: [{task['status']}]"
    return "Ошибка: задача не найдена."


def filter_tasks_by_status(tasks: list[dict], status: str) -> list[dict]:
    """Отфильтровать задачи по статусу (используется генератор/цикл)."""
    return [task for task in tasks if task.get("status") == status]


def sort_tasks_by_executor(tasks: list[dict]) -> list[dict]:
    """Отсортировать задачи по имени исполнителя (lambda-функция)."""
    return sorted(tasks, key=lambda x: x.get("executor", ""))