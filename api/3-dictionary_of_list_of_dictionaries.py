#!/usr/bin/python3
"""Export data in the CSV format."""

import json
import requests
from collections import defaultdict

if __name__ == '__main__':
    # API URL for the JSONPlaceholder service
    url = 'https://jsonplaceholder.typicode.com'

    # Make a GET request to fetch all todos with user information expanded
    response = requests.get(
        f'{url}/todos',
        params={'_expand': 'user'}
    )

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the JSON data from the response
        data = response.json()

        # Create a defaultdict to store tasks for
        # each user with user ID as the key
        dictionary = defaultdict(list)

        # Loop through the tasks data and group tasks by user ID
        for task in data:
            dictionary[task['userId']].append({
                'username': task['user']['username'],
                'task': task['title'],
                'completed': task['completed']
            })

        # Open a JSON file named 'todo_all_employees.json'
        # to store the task information
        with open('todo_all_employees.json', 'w', encoding='utf-8') as file:
            # Write the grouped tasks to the JSON file with
            # proper indentation for readability
            json.dump(dictionary, file, indent=4)

    else:
        # Display an error message if the request was not successful
        print(f"Error: {response.status_code}")
