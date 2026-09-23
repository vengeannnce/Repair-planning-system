from repairs import create_repair, find_repair_by_object, get_repair_summary
from tasks import assign_task, update_status, filter_tasks_by_status
from storage import load_data, save_data
from utils import input_int

REPAIRS_FILE = "data/repairs.json"
TASKS_FILE = "data/tasks.json"


def show_repairs(repairs: list[dict]) -> None:
    """Вывести список всех ремонтов."""
    if not repairs:
        print("Список ремонтов пуст.")
        return
    print("\n--- Список объектов и ремонтов ---")
    for r in repairs:
        status = "Активен" if r["is_active"] else "Завершен"
        print(f"ID: {r['id']} | Объект: {r['object_name']} | Площадь: {r['area']} кв.м. | Статус: {status}")


def show_tasks(tasks: list[dict]) -> None:
    """Вывести список всех задач."""
    if not tasks:
        print("Список задач пуст.")
        return
    print("\n--- Список задач ---")
    for t in tasks:
        print(f"ID: {t['id']} | Задача: {t['name']} | Исполнитель: {t['executor']} | Ремонт ID: {t['repair_id']} | Статус: {t['status']}")


def main() -> None:
    """Точка запуска приложения."""
    repairs = load_data(REPAIRS_FILE)
    tasks = load_data(TASKS_FILE)

    while True:
        print("\n=== СИСТЕМА ПЛАНИРОВАНИЯ РЕМОНТА ===")
        print("1. Создать ремонт (Добавить объект)")
        print("2. Назначить задачу исполнителю")
        print("3. Изменить статус задачи")
        print("4. Показать все объекты")
        print("5. Показать все задачи")
        print("6. Найти объект по названию")
        print("7. Показать задачи по статусу")
        print("8. Обзор состояния ремонта")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            obj_name = input("Введите название объекта (например, Кухня): ")
            try:
                area = float(input("Введите площадь (кв.м.): "))
            except ValueError:
                print("Ошибка: площадь должна быть числом.")
                continue
            create_repair(repairs, obj_name, area)
            print(f"Ремонт для объекта '{obj_name}' успешно создан!")

        elif choice == "2":
            show_repairs(repairs)
            repair_id = input_int("Введите ID объекта для назначения задачи: ")
            task_name = input("Введите название задачи (например, Укладка плитки): ")
            executor = input("Введите имя исполнителя: ")
            assign_task(tasks, task_name, executor, repair_id)
            print(f"Задача '{task_name}' назначена исполнителю {executor}.")

        elif choice == "3":
            show_tasks(tasks)
            task_id = input_int("Введите ID задачи: ")
            is_done_str = input("Задача выполнена? (да/нет): ").lower()
            is_completed = is_done_str in ["да", "yes", "y"]
            result = update_status(tasks, task_id, is_completed)
            print(result)

        elif choice == "4":
            show_repairs(repairs)

        elif choice == "5":
            show_tasks(tasks)

        elif choice == "6":
            query = input("Введите часть названия объекта для поиска: ")
            found = find_repair_by_object(repairs, query)
            if found:
                for r in found:
                    print(f"- {r['object_name']} (ID: {r['id']})")
            else:
                print("Ничего не найдено.")

        elif choice == "7":
            status = input("Введите статус (Не начато / В работе / Готово): ")
            filtered = filter_tasks_by_status(tasks, status)
            if filtered:
                for t in filtered:
                    print(f"- {t['name']} (Исполнитель: {t['executor']})")
            else:
                print(f"Задач со статусом '{status}' не найдено.")

        elif choice == "8":
            summary = get_repair_summary(repairs, tasks)
            print(f"\n{summary}")

        elif choice == "0":
            save_data(REPAIRS_FILE, repairs)
            save_data(TASKS_FILE, tasks)
            print("Данные сохранены. До свидания!")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()