from repairs import create_repair, find_repair_by_object

def test_create_repair():
    repairs = []
    create_repair(repairs, "Кухня", 15.5)
    assert len(repairs) == 1
    assert repairs[0]["object_name"] == "Кухня"
    assert repairs[0]["id"] == 1

def test_find_repair():
    repairs = []
    create_repair(repairs, "Кухня", 15.5)
    create_repair(repairs, "Ванная комната", 5.0)
    found = find_repair_by_object(repairs, "кух")
    assert len(found) == 1
    assert found[0]["object_name"] == "Кухня"