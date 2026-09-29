"""
Simple To-Do List Program
--------------------------
Features:
  1. Add a task
  2. Remove (subtract) a task
  3. Mark a task as completed
  4. Show all tasks
  5. Show only completed tasks
  6. Show only pending tasks
  0. Exit
"""

tasks = []  # each task is a dict: {"name": str, "done": bool}


def addtask():
    name = input("Enter task name: ").strip()
    if not name:
        print("Task name cannot be empty.\n")
        return
    tasks.append({"name": name, "done": False})
    print(f'Task "{name}" added.\n')



def removetask():
    showalltasks()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f'Task "{removed["name"]}" removed.\n')
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def completetask():
    showalltasks()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print(f'Task "{tasks[index]["name"]}" marked as completed.\n')
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def showalltasks():
    if not tasks:
        print("No tasks yet.\n")
        return
    print("\n All Tasks ")
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Pending"
        print(f'{i}. {task["name"]} [{status}]')
    print()


def showcompletedtasks():
    completed = [t for t in tasks if t["done"]]
    if not completed:
        print("No completed tasks yet.\n")
        return
    print("\n Completed Tasks ")
    for i, task in enumerate(completed, start=1):
        print(f'{i}. {task["name"]}')
    print()


def showpendingtasks():
    pending = [t for t in tasks if not t["done"]]
    if not pending:
        print("No pending tasks.\n")
        return
    print("\n--- Pending Tasks ---")
    for i, task in enumerate(pending, start=1):
        print(f'{i}. {task["name"]}')
    print()


def showmenu():
    print("******* TO-DO LIST MENU *******")
    print("1. Add task")
    print("2. Remove task")
    print("3. Mark task as completed")
    print("4. Show all tasks")
    print("5. Show completed tasks")
    print("6. Show pending tasks")
    print("0. Exit")


def main():
    while True:
        showmenu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            addtask()
        elif choice == "2":
            removetask()
        elif choice == "3":
            completetask()
        elif choice == "4":
            showalltasks()
        elif choice == "5":
            showcompletedtasks()
        elif choice == "6":
            showpendingtasks()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")
main()
