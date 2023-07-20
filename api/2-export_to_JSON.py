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

    employee_id = int(sys.argv[1])
    user_id, username, todos_data = getdata(employee_id)
    tasks = []
    for todo in todos_data:
        task = {
            'task': todo['title'],
            'completed': todo['completed'],
            'username': username
        }
        tasks.append(task)
    final_dic = {employee_id: tasks}
    with open(f'{employee_id}.json', 'w') as f:
        json.dump(final_dic, f)
