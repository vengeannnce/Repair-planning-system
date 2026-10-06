# Система планирования ремонта

Консольное приложение (ПР3) дополнено веб-интерфейсом на Django (ПР5).
Помогает владельцам жилья и небольшим бригадам учитывать объекты ремонта,
задачи и исполнителей, отслеживать статусы работ.

## Используемые технологии
- Python 3.11;
- Django 5.2 — веб-фреймворк;
- HTML — разметка страниц;
- CSS и Bootstrap 5.3 — оформление;
- pytest — автоматизированные тесты;
- flake8 — проверка качества кода.

## Предметная область
Основные объекты:
- **Объект / Ремонт** (`Repair`) — место и процесс работ;
- **Исполнитель** (`Executor`) — мастер или бригада;
- **Задача** (`Task`) — работа, привязанная к объекту и исполнителю,
  со статусом (Не начато / В работе / Готово).

Задача связана с объектом и исполнителем как объекты ПР3 (композиция);
в JSON хранятся только идентификаторы `repair_id` и `executor_id`,
связи восстанавливаются при загрузке.

## Основные классы (ПР3)
- `Repair` — атрибуты `id, object_name, area, is_active`;
  методы `validate_area()` (@staticmethod), `complete()`,
  `to_dict()`, `from_dict()` (@classmethod), `__str__`;
- `Executor` — атрибуты `id, name, specialization`;
  методы `to_dict()`, `from_dict()`, `__str__`;
- `Task` — атрибуты `id, name, repair, executor, status`;
  методы `start()`, `complete()`, `update_status()`,
  свойство `is_completed` (@property), `validate_status()` (@staticmethod),
  `to_dict()`, `__str__`.

## Веб-страницы (ПР5)
| Страница | URL | View |
|---|---|---|
| Главная | `/` | `homepage.views.index` |
| Список объектов | `/repairs/` | `repairs.views.repairs` |
| Объект | `/repairs/<id>/` | `repairs.views.repair_detail` |
| Список задач | `/tasks/` | `tasks.views.tasks` |
| Задача | `/tasks/<id>/` | `tasks.views.task_detail` |
| Список исполнителей | `/executors/` | `executors.views.executors` |
| Исполнитель | `/executors/<id>/` | `executors.views.executor_detail` |
| Ошибка 404 | любой несуществующий адрес | `homepage.views.page_not_found` |

## Структура проекта
```text
Repair-planning-system/
├── manage.py                 # управление Django-проектом
├── main.py                   # консольная версия (ПР3, сохранена)
├── storage.py                # JSON <-> объекты ПР3
├── utils.py                  # безопасный консольный ввод
├── repair_planning/          # настройки Django-проекта
│   ├── settings.py
│   └── urls.py               # корневая маршрутизация + handler404
├── homepage/                 # главная страница и каркас page()
├── repairs/                  # приложение объектов/ремонтов
├── tasks/                    # приложение задач
├── executors/                # приложение исполнителей
├── models/                   # классы ПР3: Repair, Executor, Task
├── data/                     # repairs.json, executors.json, tasks.json
└── tests/                    # тесты ПР3 (pytest)