# Student Task Manager

A simple Python console-based application for managing daily tasks. Users can add, view, complete, and delete tasks through an easy-to-use menu.

## Project Information

- **Project Name:** Student Task Manager
- **Developer:** Atif Khalid
- **GitHub Username:** [m-atif-khalid](https://github.com/m-atif-khalid)
- **Email:** aatifkhalid935@gmail.com
- **Repository:** [student-task-manager](https://github.com/m-atif-khalid/student-task-manager)

## Features

- Add new tasks.
- Display all tasks.
- Mark tasks as completed.
- Delete tasks.
- Validate task input.
- Run automated unit tests.
- Continuous integration using GitHub Actions.

## Technologies Used

- Python 3
- Git
- GitHub
- GitHub Issues
- GitHub Pull Requests
- GitHub Actions
- Python `unittest` framework

## Project Structure

```text
student-task-manager/
│
├── .github/
│   └── workflows/
│       └── python-tests.yml
│
├── docs/
│   └── user-guide.md
│
├── tests/
│   ├── __init__.py
│   └── test_task_manager.py
│
├── main.py
├── task_manager.py
├── README.md
├── LAB-REPORT.md
├── LICENSE
└── .gitignore
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/m-atif-khalid/student-task-manager.git
```

### 2. Open the Project Folder

```bash
cd student-task-manager
```

### 3. Run the Application

```bash
python main.py
```

## How to Use

After running the application, use the menu to:

1. Add a new task.
2. View all tasks.
3. Mark a task as completed.
4. Delete a task.
5. Exit the application.

Follow the instructions displayed in the console.

## Running Unit Tests

Run the following command from the project directory:

```bash
python -m unittest discover -s tests -v
```

The tests check task creation, task completion, task deletion, and input validation.

## GitHub Actions

This project uses GitHub Actions for automated testing.

The workflow runs when:

- Code is pushed to the `main` branch.
- A pull request is created for the `main` branch.

The workflow automatically executes the unit tests to help ensure that the application works correctly.

## Git Branches

The project uses feature branches to organize development:

- `feature/add-task` – Add new tasks.
- `feature/complete-task` – Complete existing tasks.
- `feature/delete-task` – Delete tasks.
- `feature/testing` – Add automated tests and CI workflow.
- `feature/documentation` – Improve project documentation.

Changes are integrated into the `main` branch through GitHub Pull Requests.

## Project Status

Under development as part of a DevOps for Cloud Computing assignment.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

**Atif Khalid**

- GitHub: https://github.com/m-atif-khalid
- Email: aatifkhalid935@gmail.com