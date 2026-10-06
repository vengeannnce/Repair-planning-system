"""Страницы объектов и ремонтов."""

from django.http import HttpResponse

from homepage.views import page
from models.repairs import find_repair_by_id
from storage import load_executors, load_repairs, load_tasks


def repairs(request):
    """Список объектов и ремонтов."""
    items = ""
    for repair in load_repairs("data/repairs.json"):
        status = "активен" if repair.is_active else "завершен"
        badge = "bg-success" if repair.is_active else "bg-secondary"
        items += (
            '<li class="list-group-item d-flex '
            'justify-content-between">'
            f'<a href="/repairs/{repair.id}/">'
            f"{repair.object_name} – {repair.area} кв.м."
            "</a>"
            f'<span class="badge {badge}">{status}</span>'
            "</li>"
        )
    content = f"""
    <h1>Объекты и ремонты</h1>
    <ul class="list-group">{items}</ul>
    """
    return HttpResponse(page("Объекты", content))


def repair_detail(request, repair_id):
    """Страница отдельного ремонта со связанными задачами."""
    repairs_list = load_repairs("data/repairs.json")
    repair = find_repair_by_id(repairs_list, repair_id)
    if repair is None:
        content = """
        <h1 class="text-danger">Объект не найден</h1>
        <a href="/repairs/" class="btn btn-outline-secondary">
          ← к списку объектов
        </a>
        """
        return HttpResponse(
            page("Объект не найден", content),
            status=404,
        )
    executors_list = load_executors("data/executors.json")
    tasks_list = load_tasks(
        "data/tasks.json", repairs_list, executors_list,
    )
    repair_tasks = [
        t for t in tasks_list if t.repair.id == repair.id
    ]
    items = ""
    for task in repair_tasks:
        items += (
            '<li class="list-group-item">'
            f'<a href="/tasks/{task.id}/">{task.name}</a>'
            f" – {task.executor.name} ({task.status})"
            "</li>"
        )
    if not items:
        items = (
            '<li class="list-group-item text-muted">'
            "Задачи не назначены"
            "</li>"
        )
    status = "активен" if repair.is_active else "завершен"
    badge = "bg-success" if repair.is_active else "bg-secondary"
    content = f"""
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">{repair.object_name}</h5>
        <p class="card-text">
          <strong>ID:</strong> {repair.id}
        </p>
        <p class="card-text">
          <strong>Площадь:</strong> {repair.area} кв.м.
        </p>
        <p class="card-text">
          Статус ремонта:
          <span class="badge {badge}">{status}</span>
        </p>
        <h6 class="mt-3">Задачи объекта</h6>
        <ul class="list-group">{items}</ul>
        <a href="/repairs/"
           class="btn btn-outline-secondary mt-3">
          ← к списку объектов
        </a>
      </div>
    </div>
    """
    return HttpResponse(page(repair.object_name, content))