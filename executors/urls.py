"""Маршруты приложения исполнителей."""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.executors, name="executors"),
    path(
        "<int:executor_id>/",
        views.executor_detail,
        name="executor_detail",
    ),
]