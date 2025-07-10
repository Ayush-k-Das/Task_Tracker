# ✅ Task Tracker CLI App

A command-line application to track and manage your tasks using a JSON file.

This project was built as a beginner-friendly Python CLI tool to help you practice:
- Working with the filesystem 🗂️
- Handling user inputs from command line 💬
- Reading and writing JSON data 📄
- Structuring basic CLI commands

---

## 🚀 Features

- 📌 Add new tasks  
- ✏️ Update task descriptions  
- ❌ Delete tasks  
- 🔄 Mark tasks as **in-progress** or **done**  
- 📋 List all tasks or filter by status (`todo`, `done`, `in-progress`)  
- 🧠 Tasks are stored persistently in a local `tasks.json` file  

---

## 🏁 Getting Started

### ⚙️ Requirements

- Python 3.6+
- No external libraries are required

### 📂 Setup

```bash
# Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

🛠️ Usage
➕ Add a Task
python task_tracker.py add "Buy groceries"

✏️ Update a Task
python task_tracker.py update <id> "New description"

❌ Delete a Task
python task_tracker.py delete <id>

🔄 Mark as In Progress or Done
python task_tracker.py mark-in-progress <id>
python task_tracker.py mark-done <id>

📋 List Tasks
python task_tracker.py list             # All tasks
python task_tracker.py list todo        # Only TODOs
python task_tracker.py list done        # Completed tasks
python task_tracker.py list in-progress # In-progress tasks

🧾 Task Format in JSON
Each task has:
id: Unique integer
description: Short task summary
status: todo, in-progress, or done
createdAt: ISO timestamp
updatedAt: ISO timestamp

