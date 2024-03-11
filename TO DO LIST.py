import tkinter as tk
tasks = []

def add_task():
    task = input("Enter task description: ")
    tasks.append({"description": task, "completed": False})
    print("Task added.")

def list_tasks():
    for idx, task in enumerate(tasks,start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{idx}. {task['description']} - {status}")

def update_task():
    list_tasks()
    task_number = int(input("Enter task number to update: ")) 
    if 0 <= task_number < len(tasks):
        tasks[task_number]["completed"] = not tasks[task_number]["completed"]
        print("Task updated.")
    else:
        print("Invalid task number.")

def delete_task():
    list_tasks()
    task_number = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_number < len(tasks):
        del tasks[task_number]
        print("Task deleted.")
    else:
        print("Invalid task number.")

def main():
    while True:
        action = input("Choose an action: add, list, update, delete, exit: ")
        if action == "add":
            add_task()
        elif action == "list":
            list_tasks()
        elif action == "update":
            update_task()
        elif action == "delete":
            delete_task()
        elif action == "exit":
            break
        else:
            print("Invalid action. Please choose again.")

if __name__ == "__main__":
    main()