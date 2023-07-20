#!/usr/bin/python3
import requests
import sys
EMPLOYEE_API_URL = "https://jsonplaceholder.typicode.com/users?id="
TODO_API_URL = "https://jsonplaceholder.typicode.com/todos"
EMPLOYEE_API_UR = "https://jsonplaceholder.typicode.com/users"

def getdata2(employee_id):
    
    data = requests.get(f"{EMPLOYEE_API_URL}/{employee_id}").json()
    response = requests.get(EMPLOYEE_API_URL + str(employee_id)).json()
    employe_name = response[0]['username']

    todos_data = requests.get(f"{TODO_API_URL}?userId={employee_id}").json()

    total = len(todos_data)
    tasks_completed = len([task for task in todos_data if task["completed"]])

    return employe_name, tasks_completed, total, todos_data
def getdata(employee_id):
    data = requests.get(f"{EMPLOYEE_API_UR}/{employee_id}").json()
    employe_name = data["name"]

    todos_data = requests.get(f"{TODO_API_URL}?userId={employee_id}").json()

    total = len(todos_data)
    tasks_completed = len([task for task in todos_data if task["completed"]])

    return employe_name, tasks_completed, total, todos_data
def getdata3(employee_id):
    
    data1 = requests.get(f"{EMPLOYEE_API_URL}/{employee_id}").json()
    response = requests.get(EMPLOYEE_API_URL + str(employee_id)).json()
    data = requests.get(f"{EMPLOYEE_API_UR}/{employee_id}").json()
    employe_name = response[0]['username']

    todos_data = requests.get(f"{TODO_API_URL}?userId={employee_id}").json()
    user_id =employee_id
    username=response[0]['username']

    return user_id,username, todos_data
def getdata3(employee_id):
    
    data1 = requests.get(f"{EMPLOYEE_API_URL}/{employee_id}").json()
    response = requests.get(EMPLOYEE_API_URL + str(employee_id)).json()
    data = requests.get(f"{EMPLOYEE_API_UR}/{employee_id}").json()
    employe_name = response[0]['username']

    todos_data = requests.get(f"{TODO_API_URL}?userId={employee_id}").json()
    user_id =employee_id
    username=response[0]['username']

    return user_id,username, todos_data


def printf(a):
    return [f"'{elem}'" for elem in a]
