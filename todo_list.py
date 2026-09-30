tasks = []


def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "status": "Pending"})
    print("Task added successfully!")


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\n--- TO-DO LIST ---")
    for i, item in enumerate(tasks, 1):
        print(f"{i}. {item['task']} - {item['status']}")


def update_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to update: "))

        if 1 <= number <= len(tasks):
            new_task = input("Enter new task: ")
            tasks[number - 1]["task"] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            tasks.pop(number - 1)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to complete: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["status"] = "Completed"
            print("Task completed!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


while True:
    print("\n====================")
    print("     TO-DO LIST")
    print("====================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Completed")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        complete_task()
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")
