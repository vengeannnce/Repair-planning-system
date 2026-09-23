def create_repair(repairs: list[dict], object_name: str, area: float) -> dict:
    """
    Функция из ПР1: Создание ремонта.
    Добавление нового Объекта и запуск процесса Ремонта.
    """
    new_id = max([r["id"] for r in repairs], default=0) + 1
    repair = {
        "id": new_id,
        "object_name": object_name,
        "area": area,
        "is_active": True
    }
    repairs.append(repair)
    return repair


def find_repair_by_object(repairs: list[dict], query: str) -> list[dict]:
    """Найти ремонты по подстроке названия объекта."""
    results = []
    for repair in repairs:
        if query.lower() in repair["object_name"].lower():
            results.append(repair)
    return results


def get_repair_summary(repairs: list[dict], tasks: list[dict]) -> str:
    """
    Функция из ПР1: Обзор состояния.
    Просмотр общего прогресса ремонта.
    """
    total_repairs = len(repairs)
    active_repairs = sum(1 for r in repairs if r.get("is_active"))

    total_tasks = len(tasks)
    done_tasks = sum(1 for t in tasks if t.get("status") == "Готово")
    remaining_tasks = total_tasks - done_tasks

    working_now = [t["executor"] for t in tasks if t.get("status") == "В работе"]
    workers_str = ", ".join(set(working_now)) if working_now else "Нет активных задач"

    return (f"Всего объектов: {total_repairs} (активных: {active_repairs}). "
            f"Задач: {total_tasks}, Выполнено: {done_tasks}, Осталось: {remaining_tasks}. "
            f"Сейчас работают: {workers_str}")