"""Console interface for the Student Task Manager."""
from task_manager import TaskManager

def show_menu():
    print("\n===== STUDENT TASK MANAGER =====")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

def main():
    manager = TaskManager()
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            title = input("Enter task title: ")
            try:
                task = manager.add_task(title)
                print(f"Task added successfully! ID: {task['id']}")
            except ValueError as error:
                print(error)

        elif choice == "2":
            tasks = manager.get_tasks()
            if not tasks:
                print("No tasks found.")
            else:
                for task in tasks:
                    status = "Completed" if task["completed"] else "Pending"
                    print(f"{task['id']}. {task['title']} [{status}]")

        elif choice == "3":
            task_id = input("Enter task ID to complete: ")
            if manager.complete_task(task_id):
                print("Task marked as completed.")
            else:
                print("Invalid task ID.")

        elif choice == "4":
            task_id = input("Enter task ID to delete: ")
            if manager.delete_task(task_id):
                print("Task deleted successfully.")
            else:
                print("Invalid task ID.")

        elif choice == "5":
            print("Thank you for using Student Task Manager.")
            break
        else:
            print("Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main()
