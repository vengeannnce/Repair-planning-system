import json
import os


def load_data(filename: str) -> list[dict]:
    """Загрузить данные из JSON-файла."""
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, IOError) as e:
        print(f"Ошибка чтения файла {filename}: {e}")
        return []


def save_data(filename: str, data: list[dict]) -> None:
    """Сохранить данные в JSON-файл."""
    try:
        # Создаем папку data, если её нет
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4, default=str)
    except IOError as e:
        print(f"Ошибка записи в файл {filename}: {e}")