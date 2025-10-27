TASK_FILE = "tasks.txt"

def save_tasks(tasks):
    """Save all tasks to the file."""
    with open(TASK_FILE, "w") as f:
        for task in tasks:
            f.write(f"{task['title']}|{task['status']}\n")

def load_tasks():
    """Load all tasks from the file (auto-fix old format)."""
    tasks = []
    try:
        with open(TASK_FILE, "r") as f:
            for line in f:
                parts = line.strip().split("|")

                # If line has both title and status
                if len(parts) == 2:
                    title, status = parts
                else:
                    # Old format — assume status is Pending
                    title, status = parts[0], "Pending"

                tasks.append({"title": title, "status": status})
    except FileNotFoundError:
        pass
    return tasks
