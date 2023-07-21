#!/usr/bin/python3
"""Gathering the needed information from the API."""

import csv
import json
import requests
from sys import argv

if __name__ == '__main__':
    # Make GET requests to the JSON Placeholder API
    # to fetch users and Todos data
    resp_users = requests.get('https://jsonplaceholder.typicode.com/users')
    resp_todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
    # Extract the username of the specified user from the users' response
    for i in resp_users.json():
        if i['id'] == int(argv[1]):
            emp = i['username']

    # Create a CSV file named after the user ID to store the todo information
    with open(f'{argv[1]}.csv', 'w') as f:
        # Loop through the todos' response to find todos for the specified user
        for i in resp_todos.json():
            if i['userId'] == int(argv[1]):
                # Extract the completed status and title of each todo
                c = i['completed']
                t = i['title']
                # Write the todo information to the CSV file
                f.write(f"\"{argv[1]}\",\"{emp}\",\"{c}\",\"{t}\"\n")
