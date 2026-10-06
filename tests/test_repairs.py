"""Тесты класса Repair и функций работы с ремонтами."""

from models import Repair
from models.repairs import (
    create_repair,
    find_repair_by_id,
    find_repair_by_object,
)


def test_repair_creation():
    repair = Repair(1, "Кухня", 15.5)
    assert repair.id == 1
    assert repair.object_name == "Кухня"
    assert repair.area == 15.5
    assert repair.is_active


def test_repair_str():
    repair = Repair(1, "Кухня", 15.5)
    assert "Кухня" in str(repair)


def test_validate_area():
    assert Repair.validate_area(10)
    assert not Repair.validate_area(-1)
    assert not Repair.validate_area(0)


def test_create_repair():
    repairs = []
    create_repair(repairs, "Кухня", 15.5)
    assert len(repairs) == 1
    assert isinstance(repairs[0], Repair)


def test_find_repair():
    repairs = []
    create_repair(repairs, "Кухня", 15.5)
    create_repair(repairs, "Ванная", 5.0)
    assert len(find_repair_by_object(repairs, "кух")) == 1
    assert find_repair_by_id(repairs, 2).object_name == "Ванная"