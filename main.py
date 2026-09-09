from datetime import date

# Основные данные проекта (простые типы данных)
project_name = "Ремонт кухни"
room_area = 12.5
budget_limit = 100000.0

# Данные исполнителя
worker_name = "Иван Петров"
worker_rate_per_hour = 1500.0

# Данные задачи
task_name = "Укладка плитки"
estimated_hours = 20
is_task_completed = False


# Функция 1: Проверка статуса ремонта (Ветвление)
def get_repair_status(is_completed):
    """Возвращает текстовый статус выполнения задачи."""
    if is_completed:
        return "Завершено"
    else:
        return "В работе"


# Функция 2: Расчет стоимости работ (Операции и типы) 
def calculate_work_cost(hours, rate):
    """Вычисляет стоимость работы исполнителя."""
    cost = hours * rate
    return cost


# Функция 3: Проверка бюджета (Составные условия) 
def check_budget(total_cost, limit):
    """Проверяет, укладывается ли стоимость в бюджет."""
    if total_cost <= limit:
        remaining = limit - total_cost
        return f"Бюджет в норме. Остаток: {remaining} руб."
    elif total_cost > limit:
        over_budget = total_cost - limit
        return f"Внимание! Бюджет превышен на {over_budget} руб."
    else:
        return "Ошибка расчета бюджета."


#  Главный сценарий программы
def main():
    # Вывод информации об объекте и ремонте (преобразование типов через f-строки)
    print("--- Система планирования ремонта ---")
    print(f"Объект: {project_name}")
    print(f"Площадь: {str(room_area)} кв.м.")
    
    today = date.today()
    print(f"Текущая дата: {today}")
    print("------------------------------------\n")

    # Вывод информации о задаче и исполнителе
    print(f"Текущая задача: {task_name}")
    print(f"Исполнитель: {worker_name}")
    
    # Использование Функции 1
    current_status = get_repair_status(is_task_completed)
    print(f"Статус задачи: {current_status}\n")

    # Использование Функции 2
    work_cost = calculate_work_cost(estimated_hours, worker_rate_per_hour)
    print(f"Стоимость работ: {work_cost} руб.")

    # Использование Функции 3
    budget_message = check_budget(work_cost, budget_limit)
    print(budget_message)


# Точка входа в программу
if __name__ == "__main__":
    main()