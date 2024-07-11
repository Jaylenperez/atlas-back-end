#!/usr/bin/python3
"""This module defines a script that connects to an API"""
import json
import requests
import sys


def employee_todo_list(employee_id):
    """This function exports todo list data to json"""

    site_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{site_url}/users/{employee_id}"
    todo_url = f"{site_url}/todos"
    employee_data = requests.get(employee_url).json()
    username = employee_data.get('username')

    todo_list = requests.get(todo_url, params={"userId": employee_id}).json()

    data = [{
        "task": todo['title'],
        "completed": todo['completed'],
        "username": username
    } for todo in todo_list]

    format = {str(employee_id): data}

    file = f"{employee_id}.json"
    with open(file, 'w') as f:
        json.dump(format, f)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_todo_list(int(sys.argv[1]))
