# ==============================
# Imports
# ==============================

from datetime import datetime
import json

# ==============================
# Task Class
# ==============================

class Task:

    allowed_status = ["todo", "done", "in-progress"]
    def __init__(self, id, description, status,created_at = None ,updated_at = None ):
        self.id = id
        self.description = description
        if status in self.allowed_status:
            self.status = status
        else:
            raise ValueError("Invalid status")
        if created_at is None:        
            self.created_at = datetime.now().strftime("%Y-%m-%d %I:%M %p")
        else:
            self.created_at = created_at
        self.updated_at = updated_at

# ==============================
# Global Data
# ==============================

tasks=[]

# ==============================
# JSON File Handling
# ==============================

# --------- JSON to Python ---------

def load_tasks():

    try:
        with open("tasks.json","r", encoding="utf-8") as file:
            data = json.load(file)
            for task in data:
                task_object = Task(task["id"],task["description"],task["status"], task["created_at"], task["updated_at"])
                tasks.append(task_object)

    except FileNotFoundError:
        print("No existing tasks found. Starting with an empty task list.")

    except json.JSONDecodeError:
        print("JSON file is empty or contains invalid data.")

# --------- Python to JSON ---------

def save_tasks(task_list):

    converted_tasks=[]
    for task in task_list:
        task_data= {
            "id": task.id,
            "description": task.description,
            "status": task.status,
            "created_at": task.created_at,
            "updated_at": task.updated_at
        }
        converted_tasks.append(task_data)

    with open ("tasks.json","w", encoding="utf-8") as file:
        json.dump(converted_tasks, file, indent=4)

# ==============================
# Task Operations
# ==============================
# Add Task
# View Tasks
# Update Tasks
# Delete Tasks
# Filter Tasks
# ==============================

# --------- Function to get user input for task ---------

def add_task(tasks_list):

    description = input("\nEnter the task : ").strip()
    if not description:
        print("Enter something to proceed!\n")
        return
    status = input("Enter the status of task : ").strip().lower()
    ids = []
    for task in tasks_list:
        ids.append(task.id)

    if not tasks_list:
        task_id = 1
    else:
        task_id = max(ids) + 1

    try:
        task = Task(task_id, description, status)
        tasks_list.append(task)

        print("Task added!\n")
        save_tasks(tasks_list)

    except ValueError:
        print("\nEnter a valid status!\n")

# --------- Function to display tasks ---------

def view_tasks(my_list):

    if not my_list:
        print("No tasks available to diaplay\n")
        return
    else:
        for task in my_list:
            print("\nid :", task.id)
            print("description :", task.description)
            print("status :", task.status)
            print("created_at :", task.created_at)
            if task.updated_at:
                print("Updated at:", task.updated_at)
            print("----------------------------\n")

# --------- Function update task description and status ---------

def update_task(my_list):

    if not my_list:
        print("There's no tasks to update\n")
        return
    else:
        try:
            update_id = int(input("Enter the id of task to update it : "))
        except ValueError:
            print("Please enter a numeric value!")
            return
            
    
        print("Choose option to edit task:\n1. Update task description\n2. Update task status\n")
        try:
            choice = int(input("Enter any one option :"))
        except ValueError:
            print("Enter valid option!\n")
            return

# --------- description update ---------

        if choice == 1:
    
            for task in my_list:
                if update_id == task.id:
                    new_description = input("Enter the new description : ").strip()
                    if not new_description:
                        print("Task description cannot be empty!")
                        return
                    
                    
                    task.description = new_description
                    task.updated_at = datetime.now().strftime("%Y-%m-%d %I:%M %p")
                    print("Task updated!\n")
                    save_tasks(my_list)
                    break
            else:
                print("Task ID not found!\n")
               
# --------- status update ---------

        elif choice == 2:

            for task in my_list:
                if update_id == task.id:
                    new_status = input("Enter the new status : ").strip().lower()
                    if new_status in Task.allowed_status:
                        task.status = new_status
                        task.updated_at = datetime.now().strftime("%Y-%m-%d %I:%M %p")
                        print("Task updated!\n")
                        save_tasks(my_list)
                    else:
                        print("Invalid status! Choose todo, done, or in-progress.")
                    break
            else:
                print("Task ID not found!\n")

        else:
            print("Invalid option. Please choose 1 or 2!")
            return

# --------- Function to delete tasks ---------

def delete_task(my_list):

    if not my_list:
        print("There's no tasks to delete\n")
        return
    else:
        try:
            choice = int(input("Enter the id of task to delete : "))
        except ValueError:
            print("Please enter a numeric value!\n")
            return
        for task in my_list:
            if choice == task.id:
                my_list.remove(task)
                print("Task deleted!\n")
                save_tasks(my_list)
                break
        else:
            print("Task ID not found!\n")

# --------- Filtering using status ---------

def filter_tasks_by_status(my_list):

    if not my_list:
        print("No Tasks to filter!\n")
    else:
        choice = input("Enter status to filter : ").strip().lower()
        found = False
        for task in my_list:
            if choice == task.status:
                found = True
                print("\nId :", task.id)
                print("Description :", task.description)
                print("Status :", task.status)
                print("Created_at :", task.created_at)
                if task.updated_at:
                    print("Updated at:", task.updated_at)
                print("----------------------------\n")

        if not found:
            print("No tasks found with that status!\n")

# ==============================
# Main Menu
# ==============================

def main_menu():
     
    while True:
        print("\n1. Add task \n2. View task(s) \n3. Update task \n4. Delete task \n5. Filter tasks by status \n6. Exit \n")
        try:
            choice = int(input("Enter an option: "))
        except ValueError:
            print("Please enter a numeric value!\n3")
            continue
            
        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            view_tasks(tasks)
        elif choice == 3:
            update_task(tasks)
        elif choice == 4:
            delete_task(tasks)
        elif choice == 5:
            filter_tasks_by_status(tasks)
        elif choice == 6:
            return
        else:
            print("Enter a valid option")

# ==============================
# Program Execution
# ==============================

load_tasks()
main_menu()


