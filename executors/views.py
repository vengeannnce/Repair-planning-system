"""Страницы исполнителей."""

from django.http import HttpResponse

from homepage.views import page
from models.executors import find_executor_by_id
from storage import load_executors, load_repairs, load_tasks


def executors(request):
    """Список исполнителей."""
    items = ""
    for executor in load_executors("data/executors.json"):
        items += (
            '<li class="list-group-item">'
            f'<a href="/executors/{executor.id}/">'
            f"{executor.name} – {executor.specialization}"
            "</a>"
            "</li>"
        )
    content = f"""
    <h1>Исполнители</h1>
    <ul class="list-group">{items}</ul>
    """
    return HttpResponse(page("Исполнители", content))


def executor_detail(request, executor_id):
    """Страница исполнителя со связанными задачами."""
    executors_list = load_executors("data/executors.json")
    executor = find_executor_by_id(executors_list, executor_id)
    if executor is None:
        content = """
        <h1 class="text-danger">Исполнитель не найден</h1>
        <a href="/executors/" class="btn btn-outline-secondary">
          ← к списку исполнителей
        </a>
        """
        return HttpResponse(
            page("Исполнитель не найден", content),
            status=404,
        )
    repairs_list = load_repairs("data/repairs.json")
    tasks_list = load_tasks(
        "data/tasks.json", repairs_list, executors_list,
    )
    executor_tasks = [
        t for t in tasks_list if t.executor.id == executor.id
    ]
    items = ""
    for task in executor_tasks:
        items += (
            '<li class="list-group-item">'
            f'<a href="/tasks/{task.id}/">{task.name}</a>'
            f" – {task.repair.object_name} ({task.status})"
            "</li>"
        )
    if not items:
        items = (
            '<li class="list-group-item text-muted">'
            "Задач нет"
            "</li>"
        )
    content = f"""
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">{executor.name}</h5>
        <p class="card-text">
          <strong>Специализация:</strong>
          {executor.specialization}
        </p>
        <h6 class="mt-3">Задачи исполнителя</h6>
        <ul class="list-group">{items}</ul>
        <a href="/executors/"
           class="btn btn-outline-secondary mt-3">
          ← к списку исполнителей
        </a>
      </div>
    </div>
    """
    return HttpResponse(page(executor.name, content))