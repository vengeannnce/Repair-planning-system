"""Класс Executor и функции обработки коллекции исполнителей."""


class Executor:
    """Мастер или бригада, выполняющие работы."""

    def __init__(
        self,
        executor_id: int,
        name: str,
        specialization: str,
    ) -> None:
        """Создать объект исполнителя."""
        self.id = executor_id
        self.name = name
        self.specialization = specialization

    def to_dict(self) -> dict:
        """Вернуть данные исполнителя в виде словаря."""
        return {
            "id": self.id,
            "name": self.name,
            "specialization": self.specialization,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Executor":
        """Создать объект Executor из словаря данных."""
        return cls(
            executor_id=data["id"],
            name=data["name"],
            specialization=data.get("specialization", "Мастер"),
        )

    def __str__(self) -> str:
        """Строковое представление исполнителя."""
        return (
            f"ID: {self.id} | Имя: {self.name} | "
            f"Специализация: {self.specialization}"
        )


def add_executor(
    executors: list[Executor],
    name: str,
    specialization: str,
) -> Executor:
    """Создать исполнителя и добавить в коллекцию."""
    new_id = max([e.id for e in executors], default=0) + 1
    executor = Executor(new_id, name, specialization)
    executors.append(executor)
    return executor


def find_executor_by_id(
    executors: list[Executor],
    executor_id: int,
) -> Executor | None:
    """Найти исполнителя по идентификатору."""
    for executor in executors:
        if executor.id == executor_id:
            return executor
    return None