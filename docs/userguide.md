# Student Task Manager - User Guide

## Introduction
The **Student Task Manager** is a lightweight Python console application engineered to help students organize academic tasks, deadlines, and project milestones.

## Prerequisites
- Python 3.9+ (Python 3.10 recommended)
- Git 2.x+
- Standard Unix shell (Terminal, bash, zsh) or PowerShell

## Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/HuzaifaSiddqui/studenttaskmanager.git
   cd studenttaskmanager
   ```
2. Verify Python installation:
   ```bash
   python3 --version
   ```

## Running the Application
Launch the interactive CLI interface:
```bash
python3 main.py
```

### Menu Options Walkthrough
Upon running, the console presents the main menu:
```text
========================================
       STUDENT TASK MANAGER
========================================
1. View All Tasks
2. Add New Task
3. Mark Task as Completed
4. Delete Task
5. Exit
========================================
```

1. **Option 1 (View All Tasks)**:
   - Displays all registered tasks formatted with completion indicator `[✓]` or `[ ]`, task ID, and title.
   - If no tasks exist, a warning prompt is displayed.

2. **Option 2 (Add New Task)**:
   - Prompts for a non-empty task title.
   - Trims whitespace and generates an auto-incremented numerical ID.
   - Rejects blank entries with a descriptive validation error.

3. **Option 3 (Mark Task as Completed)**:
   - Displays current tasks, then prompts for the target ID.
   - Marks the chosen task as completed `[✓]`.

4. **Option 4 (Delete Task)**:
   - Prompts for the target ID and removes the task from the collection.
   - Validates existence and displays an error if the ID is not found.

5. **Option 5 (Exit)**:
   - Gracefully exits the application.

## Running Automated Tests
Execute the unit test suite:
```bash
python3 -m unittest discover -s tests -v
```
All test cases should report `ok`.
