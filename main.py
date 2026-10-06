"""Точка входа приложения 'Система планирования ремонта'."""

from models import Executor, Repair, Task
from models.executors import add_executor, find_executor_by_id
from models.repairs import (
    create_repair,
    find_repair_by_id,
    find_repair_by_object,
)
from models.tasks import (
    assign_task,
    filter_tasks_by_status,
    get_repair_summary,
    update_task_status,
)
from storage import (
    load_executors,
    load_repairs,
    load_tasks,
    save_executors,
    save_repairs,
    save_tasks,
)
from utils import input_int

REPAIRS_FILE = "data/repairs.json"
EXECUTORS_FILE = "data/executors.json"
TASKS_FILE = "data/tasks.json"


def show_repairs(repairs: list[Repair]) -> None:
    """Вывести список ремонтов."""
    if not repairs:
        print("Список ремонтов пуст.")
        return
    print("\n--- Объекты и ремонты ---")
    for repair in repairs:
        print(repair)


def show_executors(executors: list[Executor]) -> None:
    """Вывести список исполнителей."""
    if not executors:
        print("Список исполнителей пуст.")
        return
    print("\n--- Исполнители ---")
    for executor in executors:
        print(executor)


def show_tasks(tasks: list[Task]) -> None:
    """Вывести список задач."""
    if not tasks:
        print("Список задач пуст.")
        return
    print("\n--- Задачи ---")
    for task in tasks:
        print(task)


def create_new_task(
    tasks: list[Task],
    repairs: list[Repair],
    executors: list[Executor],
) -> None:
    """Сценарий создания задачи с выбором объекта и мастера."""
    show_repairs(repairs)
    repair_id = input_int("ID ремонта: ")
    repair = find_repair_by_id(repairs, repair_id)
    if repair is None:
        print("Ошибка: ремонт не найден.")
        return

    show_executors(executors)
    executor_id = input_int("ID исполнителя: ")
    executor = find_executor_by_id(executors, executor_id)
    if executor is None:
        print("Ошибка: исполнитель не найден.")
        return

    task_name = input("Название задачи: ")
    task = assign_task(tasks, task_name, repair, executor)
    print(f"Задача создана: {task}")


def main() -> None:
    """Главное меню приложения."""
    repairs = load_repairs(REPAIRS_FILE)
    executors = load_executors(EXECUTORS_FILE)
    tasks = load_tasks(TASKS_FILE, repairs, executors)

    while True:
        print("\n=== СИСТЕМА ПЛАНИРОВАНИЯ РЕМОНТА (ООП) ===")
        print("1. Создать ремонт")
        print("2. Добавить исполнителя")
        print("3. Назначить задачу")
        print("4. Изменить статус задачи")
        print("5. Показать объекты")
        print("6. Показать исполнителей")
        print("7. Показать задачи")
        print("8. Найти объект")
        print("9. Задачи по статусу")
        print("10. Обзор состояния")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            object_name = input("Название объекта: ")
            try:
                area = float(input("Площадь (кв.м.): "))
            except ValueError:
                print("Ошибка: площадь должна быть числом.")
                continue
            if not Repair.validate_area(area):
                print("Ошибка: площадь должна быть больше 0.")
                continue
            create_repair(repairs, object_name, area)
            print("Ремонт создан!")
        elif choice == "2":
            name = input("Имя исполнителя: ")
            spec = input("Специализация: ")
            add_executor(executors, name, spec)
            print("Исполнитель добавлен!")
        elif choice == "3":
            create_new_task(tasks, repairs, executors)
        elif choice == "4":
            show_tasks(tasks)
            task_id = input_int("ID задачи: ")
            answer = input("Задача выполнена? (да/нет): ")
            is_done = answer.lower() in ("да", "yes")
            print(update_task_status(tasks, task_id, is_done))
        elif choice == "5":
            show_repairs(repairs)
        elif choice == "6":
            show_executors(executors)
        elif choice == "7":
            show_tasks(tasks)
        elif choice == "8":
            query = input("Поиск: ")
            for repair in find_repair_by_object(repairs, query):
                print(repair)
        elif choice == "9":
            status = input("Статус (Не начато / В работе / Готово): ")
            for task in filter_tasks_by_status(tasks, status):
                print(task)
        elif choice == "10":
            print(get_repair_summary(repairs, tasks))
        elif choice == "0":
            save_repairs(REPAIRS_FILE, repairs)
            save_executors(EXECUTORS_FILE, executors)
            save_tasks(TASKS_FILE, tasks)
            print("Данные сохранены. До свидания!")
            break
        else:
            print("Неверный выбор.")


if __name__ == "__main__":
    main()