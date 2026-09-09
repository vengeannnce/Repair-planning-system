from datetime import date




# Сущность: Объект
object_name = "Квартира, ул. Ленина 10"
room_area = 45.5

# Сущность: Ремонт
repair_name = "Капитальный ремонт кухни"
start_date = date.today()

# Сущности: Исполнители
executor_1 = "Иван Петров (электрик)"
executor_2 = "Бригада №1 (отделочники)"

# Сущности: Задачи и их Статусы (так как списки запрещены в ПР1, задаем переменными)
task_1_name = "Прокладка проводки"
is_task_1_completed = False

task_2_name = "Укладка плитки"
is_task_2_completed = False



# Функция 1: Создание ремонта
def create_repair(obj_name, area, rep_name):
    """Добавление нового Объекта и запуск процесса Ремонта."""
    if area > 0 and obj_name != "":
        # Преобразование типов и конкатенация строк
        info = "Ремонт '" + rep_name + "' запущен! "
        info += "Объект: " + obj_name + ", Площадь: " + str(area) + " кв.м."
        return info
    else:
        return "Ошибка: некорректные данные объекта."


# Функция 2: Управление задачами
def assign_task(task_name, executor_name):
    """Назначение на задачу конкретного Исполнителя."""
    if task_name != "" and executor_name != "":
        return f"Задача '{task_name}' назначена исполнителю: {executor_name}."
    else:
        return "Ошибка: не указано имя задачи или исполнителя."


# Функция 3: Отслеживание прогресса
def update_status(task_name, is_completed):
    """Простое переключение Статусов задач по мере их выполнения."""
    if is_completed:
        return f"Статус задачи '{task_name}' изменен на: [Готово]"
    else:
        return f"Статус задачи '{task_name}' изменен на: [В работе]"


# Функция 4: Обзор состояния
def show_summary(t1_name, t1_done, t1_executor, t2_name, t2_done, t2_executor):
    """Просмотр общего прогресса ремонта (сколько сделано, осталось, кто работает)."""
    total_tasks = 2
    done_count = 0
    
    # Подсчет выполненных задач без использования циклов и списков
    if t1_done:
        done_count = done_count + 1
    if t2_done:
        done_count = done_count + 1
        
    remaining = total_tasks - done_count
    
    # Определение того, кто сейчас работает
    working_now = ""
    if not t1_done:
        working_now = working_now + t1_executor + ", "
    if not t2_done:
        working_now = working_now + t2_executor
        
    if working_now == "":
        working_now = "Нет активных задач, все завершено!"
        
    return f"ОБЗОР: Выполнено {done_count} из {total_tasks}. Осталось: {remaining}. Сейчас работают: {working_now}"



# ГЛАВНЫЙ СЦЕНАРИЙ ПРОГРАММЫ
def main():
    print("СИСТЕМА ПЛАНИРОВАНИЯ РЕМОНТА\n")
    print(f"Дата запуска: {start_date}\n")

    # 1. Вызов функции "Создание ремонта"
    print("--- 1. СОЗДАНИЕ РЕМОНТА ---")
    repair_info = create_repair(object_name, room_area, repair_name)
    print(repair_info)
    print("-" * 40 + "\n")

    # 2. Вызов функции "Управление задачами"
    print("--- 2. УПРАВЛЕНИЕ ЗАДАЧАМИ ---")
    print(assign_task(task_1_name, executor_1))
    print(assign_task(task_2_name, executor_2))
    print("-" * 40 + "\n")

    # 3. Вызов функции "Отслеживание прогресса"
    print("--- 3. ОТСЛЕЖИВАНИЕ ПРОГРЕССА ---")
    print(update_status(task_1_name, is_task_1_completed))
    print(update_status(task_2_name, is_task_2_completed))
    
    # Имитируем выполнение первой задачи
    print("\n... Прошло время, первая задача выполнена ... \n")
    is_task_1_completed = True
    print(update_status(task_1_name, is_task_1_completed))
    print("-" * 40 + "\n")

    # 4. Вызов функции "Обзор состояния"
    print("--- 4. ОБЗОР СОСТОЯНИЯ ---")
    summary = show_summary(
        task_1_name, is_task_1_completed, executor_1,
        task_2_name, is_task_2_completed, executor_2
    )
    print(summary)
    
    print("\n=== СЦЕНАРИЙ ЗАВЕРШЕН ===")


# Точка входа в программу
if __name__ == "__main__":
    main()