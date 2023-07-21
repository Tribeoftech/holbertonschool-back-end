#!/usr/bin/python3
"""Export data in the CSV format."""

import json
import requests
from sys import argv

if __name__ == '__main__':
    # Get the user ID from the command-line argument
    user_id = argv[1]

    # API URL for the JSONPlaceholder service
    url = 'https://jsonplaceholder.typicode.com'

    # Make a GET request to fetch the user's TODO list with
    # user information expanded
    response = requests.get(
        f'{url}/users/{user_id}/todos',
        params={'_expand': 'user'}
    )

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the JSON data from the response
        data = response.json()

        # Create a dictionary to store the tasks for the user
        # with their user ID as the key
        user_tasks = {user_id: []}

        # Open a JSON file named after user ID to store the task information
        with open(f'{user_id}.json', 'w', encoding='utf-8') as file:
            # Loop through the tasks data and extract relevant information
            for task in data:
                task_info = {
                    'task': task['title'],
                    'completed': task['completed'],
                    'username': task['user']['username']
                }
                # Append the task information to the user_tasks dictionary
                user_tasks[user_id].append(task_info)

            # Write the user_tasks dictionary to the JSON file
            json.dump(user_tasks, file)

    else:
        # Display an error message if the request was not successful
        print(f"Error: {response.status_code}")
