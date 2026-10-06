"""Маршруты приложения объектов и ремонтов."""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.repairs, name="repairs"),
    path(
        "<int:repair_id>/",
        views.repair_detail,
        name="repair_detail",
    ),
]