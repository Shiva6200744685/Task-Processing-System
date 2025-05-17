# Task Processing System

## 📝 Overview
The **Task Processing System** is a lightweight, modular tool designed to read task information from JSON files and generate structured log outputs. This project emphasizes clean code, reusability, and easy integration into larger systems or pipelines.

---

## 📁 Core Components

### 1. `task_processor.py`
- Converts JSON task data into a clean, formatted log output.
- Handles essential fields such as:
  - `task_id`
  - `script`
  - `action`
- Ensures consistency and readability in all logs.

### 2. `main.py`
- Reads and parses task data from a JSON file.
- Delegates formatting to the task processor.
- Writes the final formatted log to a text file.
- Provides a reusable API for integration into other applications.

---

## 🔄 Workflow

1. Read task data from a JSON file (e.g., `task.json`)
2. Process the task using `task_processor.py`
3. Output the result into a log file (e.g., `log.txt`)

---

## 📥 Sample Input (`task.json`)
```json
{
    "task_id": "001",
    "action": "start_script",
    "script": "monitor.py"
}
