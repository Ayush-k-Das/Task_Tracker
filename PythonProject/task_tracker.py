import json
import os
import sys
from datetime import datetime

# File to store tasks
TASK_FILE = "tasks.json"

# Step 1: Ensure tasks.json exists
if not os.path.exists(TASK_FILE):
    with open(TASK_FILE, "w") as file:
        json.dump([], file)

# Step 2: Load tasks from JSON
with open(TASK_FILE, "r") as file:
    try:
        tasks = json.load(file)
    except json.JSONDecodeError:
        tasks = []

# Step 3: Handle 'add' command
if len(sys.argv) >= 3 and sys.argv[1] == "add":
    description = sys.argv[2]

    next_id = max([task["id"] for task in tasks], default=0) + 1
    now = datetime.now().isoformat()

    new_task = {
        "id": next_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }

    tasks.append(new_task)

    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

    print(f"✅ Task added successfully (ID: {next_id})")

# Step 4: Handle 'list' and optional status filter
elif len(sys.argv) >= 2 and sys.argv[1] == "list":
    status_filter = sys.argv[2].lower() if len(sys.argv) == 3 else None

    if status_filter and status_filter not in ["todo", "done", "in-progress"]:
        print("⚠️  Invalid status filter. Use: todo, done, or in-progress.")
        sys.exit(1)

    filtered_tasks = [task for task in tasks if task["status"] == status_filter] if status_filter else tasks

    if not filtered_tasks:
        print("📂 No matching tasks found.")
    else:
        for task in filtered_tasks:
            print(f"🆔 ID: {task['id']}")
            print(f"📋 Description: {task['description']}")
            print(f"📌 Status: {task['status']}")
            print(f"📅 Created At: {task.get('createdAt', 'N/A')}")
            print(f"🕒 Updated At: {task.get('updatedAt', 'N/A')}")
            print("-" * 30)

# Step 5: Handle 'update' command
elif len(sys.argv) >= 4 and sys.argv[1] == "update":
    try:
        task_id = int(sys.argv[2])
        new_description = sys.argv[3]
    except ValueError:
        print("⚠️  Invalid task ID.")
        sys.exit(1)

    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            with open(TASK_FILE, "w") as file:
                json.dump(tasks, file, indent=4)
            print(f"✅ Task {task_id} updated successfully.")
            break
    else:
        print(f"❌ Task with ID {task_id} not found.")

# Step 6: Handle 'delete' command
elif len(sys.argv) >= 3 and sys.argv[1] == "delete":
    try:
        task_id = int(sys.argv[2])
    except ValueError:
        print("⚠️  Invalid task ID.")
        sys.exit(1)

    updated_tasks = [task for task in tasks if task["id"] != task_id]

    if len(updated_tasks) == len(tasks):
        print(f"❌ Task with ID {task_id} not found.")
    else:
        with open(TASK_FILE, "w") as file:
            json.dump(updated_tasks, file, indent=4)
        print(f"✅ Task {task_id} deleted successfully.")

# Step 7: Handle 'mark-in-progress' and 'mark-done'
elif len(sys.argv) >= 3 and sys.argv[1] in ["mark-in-progress", "mark-done"]:
    try:
        task_id = int(sys.argv[2])
    except ValueError:
        print("⚠️  Invalid task ID.")
        sys.exit(1)

    new_status = "in-progress" if sys.argv[1] == "mark-in-progress" else "done"

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            task["updatedAt"] = datetime.now().isoformat()
            with open(TASK_FILE, "w") as file:
                json.dump(tasks, file, indent=4)
            print(f"✅ Task {task_id} marked as {new_status}.")
            break
    else:
        print(f"❌ Task with ID {task_id} not found.")

# Fallback for unknown commands
else:
    print("❗ Invalid command. Please use one of the following:")
    print("   add <description>")
    print("   update <id> <new_description>")
    print("   delete <id>")
    print("   mark-in-progress <id>")
    print("   mark-done <id>")
    print("   list [todo|done|in-progress]")
