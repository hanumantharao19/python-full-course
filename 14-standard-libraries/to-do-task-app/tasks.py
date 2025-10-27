from file_handler import save_tasks, load_tasks

def add_task(tasks):
    """Add a new task."""
    title = input("Enter new task: ")
    tasks.append({"title": title, "status": "Pending"})
    save_tasks(tasks)
    print(f"✅ Task '{title}' added successfully!")


def view_tasks(tasks):
    """View all tasks."""
    if not tasks:
        print("📭 No tasks available.")
    else:
        print("\n📝 Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['title']} — {task['status']}")


def mark_complete(tasks):
    """Mark a task as completed."""
    view_tasks(tasks)
    try:
        task_no = int(input("\nEnter task number to mark complete: "))
        if 1 <= task_no <= len(tasks):
            tasks[task_no - 1]["status"] = "Completed"
            save_tasks(tasks)
            print(f"✅ Task '{tasks[task_no - 1]['title']}' marked as completed!")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")


def delete_task(tasks):
    """Delete a task by its number."""
    view_tasks(tasks)
    try:
        task_no = int(input("\nEnter task number to delete: "))
        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            save_tasks(tasks)
            print(f"🗑️ Task '{removed['title']}' deleted successfully!")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")
