# Student Task Manager

![Python Unit Tests](https://github.com/HuzaifaSiddqui/studenttaskmanager/actions/workflows/python-tests.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Version](https://img.shields.io/badge/Release-v1.0.0-green.svg)

A modular Python console application for student task management built with rigorous DevOps practices including Git version control, GitHub Issues, Pull Request code reviews, automated CI via GitHub Actions, and semantic release publishing.

---

## Features
- **Task Addition with Validation**: Creates tasks with auto-incremented IDs and enforces non-empty titles.
- **Task Listing**: Displays active and completed tasks with intuitive status flags (`[✓]` / `[ ]`).
- **Status Toggle**: Marks existing tasks as completed by ID.
- **Task Deletion**: Removes tasks safely by identifier with bounds checking.
- **Automated Testing**: 7 comprehensive unit test cases covering happy paths and exception handling.
- **CI/CD Pipeline**: GitHub Actions workflow automatically testing code on push and PR events.

---

## Project Status
Project status: Active Development & Quality Review

---

## Quick Start Guide

### Prerequisites
- Python 3.9+ (Python 3.10 recommended)
- Git 2.x+

### 1. Clone Repository
```bash
git clone https://github.com/HuzaifaSiddqui/studenttaskmanager.git
cd studenttaskmanager
```

### 2. Run the Application
Launch the console interface:
```bash
python3 main.py
```

### 3. Run Automated Tests
Execute the unit test discovery suite:
```bash
python3 -m unittest discover -s tests -v
```

---

## Documentation Links
- **[User Guide](docs/userguide.md)**: Detailed step-by-step user walkthrough and operational examples.
- **[Lab Report](LABREPORT.md)**: Complete analysis of Git vs. GitHub, branching, PRs, merge conflict resolution, CI/CD, and team collaboration.
- **[Evidence Directory](labevidence/)**: Contains raw logs and evidence files demonstrating conflict resolution, test outputs, and GitHub Actions CI traces.

---

## License
This project is open-source and licensed under the [MIT License](LICENSE).
