#!/usr/bin/python3
"""
For a given employee ID,
returns information about his/her TODO list progress.

Exports data in the JSON format and creates a dictionary.
"""
import json
import requests


def fetch_user_data(user_id):
    """Fetch user data from the API"""
    base_url = 'https://jsonplaceholder.typicode.com'
    todo_url = f"{base_url}/users/{user_id}/todos"
    employee_url = f"{base_url}/users/{user_id}"

    # Fetching user and todo data
    users_response = requests.get(employee_url)
    todo_response = requests.get(todo_url)

    # Checking if requests were successful
    if users_response.status_code != 200 or todo_response.status_code != 200:
        return None, None

    employee_data = users_response.json()
    todo_data = todo_response.json()

    return employee_data, todo_data


def create_user_dict(user_id, name, tasks):
    """Creates a dictionary for a user"""
    return {
        user_id: [
            {
                'username': name,
                'task': task,
            }
            for task in tasks.items()
        ]
    }


def dict_of_dicts():
    """Gathering data from the API and exporting to JSON."""
    all_dict = {}

    for user_id in range(1, 11):
        employee_data, todo_data = fetch_user_data(user_id)

        # Skip if the API request was unsuccessful.
        if employee_data is None or todo_data is None:
            print(f"Failed to fetch data for user {user_id}")
            continue

        name = employee_data.get("username")
        tasks = {task["title"]: task['completed'] for task in todo_data}

        new_dict = create_user_dict(user_id, name, tasks)
        all_dict.update(new_dict)

    with open("todo_all_employees.json", "w") as newfile:
        json.dump(all_dict, newfile)


if __name__ == "__main__":
    dict_of_dicts()