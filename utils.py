from datetime import date, datetime


def input_int(prompt: str) -> int:
    """Запросить у пользователя целое число с обработкой ошибок."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Ошибка: введите целое число.")


def input_date(prompt: str) -> date:
    """Запросить у пользователя дату в формате ДД.ММ.ГГГГ."""
    while True:
        date_str = input(prompt)
        try:
            parsed_date = datetime.strptime(date_str, "%d.%m.%Y").date()
            return parsed_date
        except ValueError:
            print("Ошибка: неверный формат даты. Используйте ДД.ММ.ГГГГ.")