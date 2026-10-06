"""Класс Repair и функции обработки коллекции ремонтов."""


class Repair:
    """Объект недвижимости и процесс ремонта на нем."""

    def __init__(
        self,
        repair_id: int,
        object_name: str,
        area: float,
        is_active: bool = True,
    ) -> None:
        """Создать объект ремонта."""
        self.id = repair_id
        self.object_name = object_name
        self.area = area
        self.is_active = is_active

    @staticmethod
    def validate_area(area: float) -> bool:
        """Проверить корректность площади."""
        return isinstance(area, (int, float)) and area > 0

    def complete(self) -> None:
        """Отметить ремонт как завершенный."""
        self.is_active = False

    def to_dict(self) -> dict:
        """Вернуть данные объекта в виде словаря для JSON."""
        return {
            "id": self.id,
            "object_name": self.object_name,
            "area": self.area,
            "is_active": self.is_active,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Repair":
        """Создать объект Repair из словаря данных."""
        return cls(
            repair_id=data["id"],
            object_name=data["object_name"],
            area=data["area"],
            is_active=data.get("is_active", True),
        )

    def __str__(self) -> str:
        """Строковое представление ремонта."""
        status = "активен" if self.is_active else "завершен"
        return (
            f"ID: {self.id} | Объект: {self.object_name} | "
            f"Площадь: {self.area} кв.м. | Ремонт: {status}"
        )


def create_repair(
    repairs: list[Repair],
    object_name: str,
    area: float,
) -> Repair:
    """Создать ремонт и добавить его в коллекцию."""
    new_id = max([r.id for r in repairs], default=0) + 1
    repair = Repair(new_id, object_name, area)
    repairs.append(repair)
    return repair


def find_repair_by_object(
    repairs: list[Repair],
    query: str,
) -> list[Repair]:
    """Найти ремонты по подстроке названия объекта."""
    return [
        r for r in repairs
        if query.lower() in r.object_name.lower()
    ]


def find_repair_by_id(
    repairs: list[Repair],
    repair_id: int,
) -> Repair | None:
    """Найти ремонт по идентификатору."""
    for repair in repairs:
        if repair.id == repair_id:
            return repair
    return None