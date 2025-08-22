# todo.py
def add_task(task):
    with open("tasks.txt", "a") as f:
        f.write(task + "\n")

def show_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
        if not tasks:
            print("No tasks yet.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks file found. Add a task first!")

if __name__ == "__main__":
    while True:
        choice = input("\n1. Add Task  2. Show Tasks  3. Exit\nChoose: ")
        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")
