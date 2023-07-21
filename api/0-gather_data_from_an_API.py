#!/usr/bin/python3
"""returns information about his/her TODO list progress."""
import requests
from sys import argv

if __name__ == '__main__':
    # API URL for the JSONPlaceholder service
    url = 'https://jsonplaceholder.typicode.com'

    # Get the user ID from the command-line argument
    user_id = argv[1]

    # Make a GET request to fetch the user's TODO list with user information
    response = requests.get(
        f'{url}/users/{user_id}/todos',
        params={'_expand': 'user'}
    )

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the JSON data from the response
        data = response.json()

        # Get the name of the user from the first task
        # (assuming all tasks belong to the same user)
        name = data[0]['user']['name']

        # Filter tasks that are completed (completed = True)
        tasks_ok = [task for task in data if task['completed']]

        # Get the number of completed tasks and the total number of tasks
        n_task_ok = len(tasks_ok)
        total_task = len(data)

        # First line to display the user's name and progress
        first_str = f"Employee {name} is done with tasks"

        # Display progress information
        print(f"{first_str} ({n_task_ok}/{total_task}):")

        # Display the titles of completed tasks
        for task in tasks_ok:
            print(f"\t {task['title']}")

    else:
        # Display an error message if the request was not successful
        print(f"Error: {response.status_code}")
