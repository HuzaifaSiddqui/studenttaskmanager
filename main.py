"""
Student Task Manager - Console User Interface
"""
import sys
from task_manager import TaskManager


def show_menu():
    print("\n" + "=" * 40)
    print("       STUDENT TASK MANAGER")
    print("=" * 40)
    print("1. View All Tasks")
    print("2. Add New Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    print("=" * 40)


def view_tasks_flow(manager: TaskManager):
    tasks = manager.get_all_tasks()
    if not tasks:
        print("\n[!] No tasks found. Add a new task to get started.")
        return
    print("\n--- Current Tasks ---")
    for t in tasks:
        print(f"  {t}")


def add_task_flow(manager: TaskManager):
    title = input("Enter task title: ")
    try:
        task = manager.add_task(title)
        print(f"[✓] Successfully added task #{task.id}: '{task.title}'")
    except ValueError as err:
        print(f"[✗] Validation Error: {err}")


def complete_task_flow(manager: TaskManager):
    view_tasks_flow(manager)
    val = input("\nEnter task ID to mark completed: ").strip()
    try:
        task_id = int(val)
        manager.complete_task(task_id)
        print(f"[✓] Task #{task_id} marked as completed.")
    except ValueError:
        print("[✗] Error: Please enter a valid numerical ID.")
    except KeyError as err:
        print(f"[✗] Error: {err}")


def delete_task_flow(manager: TaskManager):
    view_tasks_flow(manager)
    val = input("\nEnter task ID to delete: ").strip()
    try:
        task_id = int(val)
        manager.delete_task(task_id)
        print(f"[✓] Task #{task_id} deleted successfully.")
    except ValueError:
        print("[✗] Error: Please enter a valid numerical ID.")
    except KeyError as err:
        print(f"[✗] Error: {err}")


def run_cli():
    manager = TaskManager()
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()
        if choice == "1":
            view_tasks_flow(manager)
        elif choice == "2":
            add_task_flow(manager)
        elif choice == "3":
            complete_task_flow(manager)
        elif choice == "4":
            delete_task_flow(manager)
        elif choice == "5":
            print("\nExiting Student Task Manager. Goodbye!")
            sys.exit(0)
        else:
            print("[✗] Invalid option. Please select 1 through 5.")


if __name__ == "__main__":
    run_cli()
