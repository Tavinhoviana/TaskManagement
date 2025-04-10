def add_task(tasks, task_name):
    task = {"task": task_name, "completed": False}
    tasks.append(task)
    print(f"Task '{task_name}' was successfully added!")
    return

def view_tasks(tasks):
    print("\nTask list:")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "
        task_name = task["task"]
        print(f"{index}. [{status}] {task_name}")
    return

def update_task_name(tasks, task_index, new_task_name):
    adjusted_index = int(task_index) - 1
    if 0 <= adjusted_index < len(tasks):
        tasks[adjusted_index]["task"] = new_task_name
        print(f"Task {task_index} updated to '{new_task_name}'")
    else:
        print("Invalid task index.")
    return

def complete_task(tasks, task_index):
    adjusted_index = int(task_index) - 1
    tasks[adjusted_index]["completed"] = True
    print(f"Task {task_index} marked as completed")
    return

def delete_completed_tasks(tasks):
    # To avoid issues while removing from the list you're iterating over,
    # it's better to create a new list with only incomplete tasks
    tasks[:] = [task for task in tasks if not task["completed"]]
    print("Completed tasks have been deleted.")
    return

tasks = []
while True:
    print("\nTaskbar Manager Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Update task")
    print("4. Complete task")
    print("5. Delete completed tasks")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task_name = input("Enter the task you want to add: ")
        add_task(tasks, task_name)

    elif choice == "2":
        view_tasks(tasks)

    elif choice == "3":
        view_tasks(tasks)
        task_index = input("Enter the number of the task you want to update: ")
        new_name = input("Enter the new name of the task: ")
        update_task_name(tasks, task_index, new_name)

    elif choice == "4":
        view_tasks(tasks)
        task_index = input("Enter the number of the task you want to complete: ")
        complete_task(tasks, task_index)
    
    elif choice == "5":
        delete_completed_tasks(tasks)
        view_tasks(tasks)

    elif choice == "6":
        break

print("Program ended!")
