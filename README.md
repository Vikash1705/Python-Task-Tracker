# Python CLI Task Tracker

A simple command-line Task Tracker application built using Python. It allows users to create, view, update, delete, and filter tasks while maintaining task information using JSON file storage.

## Features

* **Add Tasks:** Create tasks with a description and status.
* **View Tasks:** Display all available tasks with their details.
* **Update Tasks:** Modify task descriptions and statuses.
* **Delete Tasks:** Remove tasks using their unique IDs.
* **Filter Tasks:** Filter tasks based on their status.
* **Unique IDs:** Automatically generate unique task IDs.
* **Timestamps:** Track task creation and modification times.
* **Data Persistence:** Store tasks in a JSON file so they remain available after restarting the application.
* **Input Validation:** Handle empty descriptions, invalid statuses, and unexpected numeric inputs.

## Technologies Used

* Python
* JSON
* Datetime module

## Task Statuses

The application supports three task statuses:

| Status        | Description                       |
| ------------- | --------------------------------- |
| `todo`        | Task is yet to be started         |
| `in-progress` | Task is currently being worked on |
| `done`        | Task has been completed           |

## Project Structure

```text
TaskTracker/
│
├── main.py       # Main application
├── tasks.json    # Stores task data
└── README.md     # Project documentation
```

## Getting Started

### Prerequisites

* Python 3 installed on your system.
* A code editor or terminal.

### Installation

1. Clone this repository:

```bash
git clone YOUR_REPOSITORY_URL
```

2. Navigate to the project directory:

```bash
cd TaskTracker
```

3. Run the application:

```bash
python main.py
```

No external Python packages are required.

## How to Use

After running the application, the following menu appears:

```text
1. Add task
2. View task(s)
3. Update task
4. Delete task
5. Filter tasks by status
6. Exit
```

Select an option by entering its corresponding number.

### Data Storage

Tasks are stored in `tasks.json` using JSON serialization.

The application loads previously saved tasks when it starts and saves changes whenever tasks are added, updated, or deleted.

## Concepts Practiced

This project helped me practise:

* Object-Oriented Programming (OOP)
* Classes and Objects
* Functions
* Lists and Dictionaries
* Loops and Conditional Statements
* Exception Handling
* File Handling
* JSON Serialization and Deserialization
* Date and Time Handling
* Input Validation

## Future Improvements

* Organize the application into multiple Python modules.
* Add task priorities.
* Add due dates and deadlines.
* Implement task searching.
* Improve input validation and error handling.

## Author

Developed as a personal Python learning project.
