# test_todo.py
import os
import todo

def test_add_and_show_tasks(tmp_path):
    # Change working directory to a temp folder
    os.chdir(str(tmp_path))

    # Add tasks
    todo.add_task("Task 1")
    todo.add_task("Task 2")

    # Read file and check contents
    with open("tasks.txt") as f:
        tasks = f.read().strip().split("\n")

    assert tasks == ["Task 1", "Task 2"]
