#!/usr/bin/python3
"""Gathering the needed informations from the API."""
import csv
import json
import requests
from sys import argv

if __name__ == '__main__':
    resp_users = requests.get('https://jsonplaceholder.typicode.com/users')
    resp_todos = requests.get('https://jsonplaceholder.typicode.com/todos/')

    for i in resp_users.json():
        if i['id'] == int(argv[1]):
            emp = i['username']
    with open(f'{argv[1]}.csv', 'w') as f:
        for i in resp_todos.json():
            if i['userId'] == int(argv[1]):
                c = i['completed']
                t = i['title']
                f.write(f"\"{argv[1]}\",\"{emp}\",\"{c}\",\"{t}\"\n")
