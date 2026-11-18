# Student Task Manager

A simple Python console application for managing student tasks.

## Features
- Add tasks with a non-empty title
- Display all tasks and their status
- Mark a task as completed
- Delete a task by its ID
- Validate task titles and task identifiers

## Requirements
- Python 3.8 or newer
- Git (for version-control activities)

## Setup
1. Clone the repository:
   `git clone https://github.com/YOUR-USERNAME/student-task-manager.git`
2. Open the project folder:
   `cd student-task-manager`
3. Run the application:
   `python main.py`

## Usage
Run `python main.py` and select an option from the menu. Tasks are kept in memory while the program is running; they are not saved after the application exits.

## Run tests
`python -m unittest discover -s tests -v`

## GitHub Actions
The workflow in `.github/workflows/python-tests.yml` runs the unit tests on pushes to `main` and pull requests targeting `main`.

## License
This project is licensed under the MIT License.

## Project Status
Project status: Completed