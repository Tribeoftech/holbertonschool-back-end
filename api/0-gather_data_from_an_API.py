#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a
given employee ID, returns information about his/her TODO
list progress.
"""
import requests
import sys
if __name__ == "__main__":
    # Retrieve employee data
    employee_id = int(sys.argv[1])
    employee_data = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}").json()
    EMPLOYEE_NAME = employee_data["name"]

    # Retrieve todo list for employee
    adress = "https://jsonplaceholder.typicode.com/todos?userId="
    todos_data = requests.get(
        f"{adress}{employee_id}").json()
    # Calculate progress
    TOTAL_NUMBER_OF_TASKS = len(todos_data)
    NUMBER_OF_DONE_TASKS = len(
        [task for task in todos_data if task["completed"] is True])
    progress = f"{NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}"

    # Print progress and completed tasks
    print(f"Employee {EMPLOYEE_NAME} is done with tasks({progress}):")
    for TASK_TITLE in todos_data:
        if TASK_TITLE["completed"] is True:
            print(f"\t {TASK_TITLE['title']}")
