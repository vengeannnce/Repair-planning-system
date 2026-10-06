"""Главная страница и общий каркас HTML-страниц."""

from django.http import HttpResponse

BOOTSTRAP = (
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3"
    "/dist/css/bootstrap.min.css"
)


def page(title: str, content: str) -> str:
    """Собрать HTML-документ с навигацией и Bootstrap."""
    nav = """
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container">
        <a class="navbar-brand" href="/">Ремонт</a>
        <div class="navbar-nav">
          <a class="nav-link" href="/">Главная</a>
          <a class="nav-link" href="/repairs/">Объекты</a>
          <a class="nav-link" href="/tasks/">Задачи</a>
          <a class="nav-link" href="/executors/">Исполнители</a>
        </div>
      </div>
    </nav>
    """
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport"
        content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <link rel="stylesheet" href="{BOOTSTRAP}">
</head>
<body>
{nav}
  <main class="container py-4">
{content}
  </main>
</body>
</html>"""


def index(request):
    """Главная страница приложения."""
    content = """
    <h1 class="display-4">Система планирования ремонта</h1>
    <p class="lead">Учёт объектов, задач и исполнителей.</p>
    <p>Основные разделы:</p>
    <a href="/repairs/" class="btn btn-primary me-2">Объекты</a>
    <a href="/tasks/" class="btn btn-secondary me-2">Задачи</a>
    <a href="/executors/" class="btn btn-outline-secondary">
      Исполнители
    </a>
    """
    return HttpResponse(page("Система ремонта", content))


def page_not_found(request, exception):
    """Обработчик ошибки 404 для всего проекта."""
    content = """
    <h1 class="text-danger">Страница не найдена</h1>
    <a href="/" class="btn btn-outline-secondary">
      ← на главную
    </a>
    """
    return HttpResponse(
        page("Страница не найдена", content),
        status=404,
    )