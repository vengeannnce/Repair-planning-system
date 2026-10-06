"""Страницы задач ремонта."""

from django.http import HttpResponse

from homepage.views import page
from models.tasks import find_task_by_id
from storage import load_executors, load_repairs, load_tasks


def _status_badge(status: str) -> str:
    """Вернуть CSS-класс бейджа по статусу задачи."""
    if status == "Готово":
        return "bg-success"
    if status == "В работе":
        return "bg-warning"
    return "bg-secondary"


def tasks(request):
    """Список всех задач."""
    repairs_list = load_repairs("data/repairs.json")
    executors_list = load_executors("data/executors.json")
    tasks_list = load_tasks(
        "data/tasks.json", repairs_list, executors_list,
    )
    items = ""
    for task in tasks_list:
        badge = _status_badge(task.status)
        items += (
            '<li class="list-group-item d-flex '
            'justify-content-between">'
            f'<a href="/tasks/{task.id}/">'
            f"{task.name} – {task.executor.name}"
            "</a>"
            f'<span class="badge {badge}">{task.status}</span>'
            "</li>"
        )
    content = f"""
    <h1>Задачи</h1>
    <ul class="list-group">{items}</ul>
    """
    return HttpResponse(page("Задачи", content))


def task_detail(request, task_id):
    """Страница отдельной задачи (связи через объекты ПР3)."""
    repairs_list = load_repairs("data/repairs.json")
    executors_list = load_executors("data/executors.json")
    tasks_list = load_tasks(
        "data/tasks.json", repairs_list, executors_list,
    )
    task = find_task_by_id(tasks_list, task_id)
    if task is None:
        content = """
        <h1 class="text-danger">Задача не найдена</h1>
        <a href="/tasks/" class="btn btn-outline-secondary">
          ← к списку задач
        </a>
        """
        return HttpResponse(
            page("Задача не найдена", content),
            status=404,
        )
    badge = _status_badge(task.status)
    content = f"""
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">Задача №{task.id}</h5>
        <p class="card-text">
          <strong>Название:</strong> {task.name}
        </p>
        <p class="card-text">
          <strong>Объект:</strong> {task.repair.object_name}
        </p>
        <p class="card-text">
          <strong>Исполнитель:</strong> {task.executor.name}
        </p>
        <p class="card-text">
          Статус:
          <span class="badge {badge}">{task.status}</span>
        </p>
        <a href="/tasks/" class="btn btn-outline-secondary">
          ← к списку задач
        </a>
      </div>
    </div>
    """
    return HttpResponse(page(task.name, content))