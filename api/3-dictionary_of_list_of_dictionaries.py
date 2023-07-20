#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script
to export data in the CSV format.
"""

if __name__ == '__main__':
    import requests
    import sys
    import csv
    import importlib
    import json
    from funct import getdata3, printf
    module = importlib.import_module('funct')
    getdata = module.getdata3
    all_tasks = {}
    for i in range(1, 11):
        employee_id = i
        user_id, username, todos_data = getdata(employee_id)
        tasks = []
        for todo in todos_data:
            task = {
                'username': username,
                'task': todo['title'],
                'completed': todo['completed'],

            }
            tasks.append(task)
            all_tasks[employee_id] = tasks
        with open(f'todo_all_employees.json', 'w') as f:
            json.dump(all_tasks, f)
