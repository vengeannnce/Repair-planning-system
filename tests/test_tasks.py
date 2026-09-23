from tasks import assign_task, update_status, filter_tasks_by_status

def test_assign_task():
    tasks = []
    assign_task(tasks, "Штукатурка", "Иван", 1)
    assert len(tasks) == 1
    assert tasks[0]["status"] == "Не начато"

def test_update_status():
    tasks = []
    assign_task(tasks, "Штукатурка", "Иван", 1)
    update_status(tasks, 1, True)
    assert tasks[0]["status"] == "Готово"

def test_filter_tasks():
    tasks = []
    assign_task(tasks, "Задача 1", "Иван", 1)
    assign_task(tasks, "Задача 2", "Петр", 1)
    update_status(tasks, 1, True)
    
    done_tasks = filter_tasks_by_status(tasks, "Готово")
    assert len(done_tasks) == 1
    assert done_tasks[0]["name"] == "Задача 1"