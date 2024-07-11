#!/usr/bin/python3
"""
For a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests
import sys


def employee_todo_list(employee_id):
    """
    Fetch and display the TODO list progress of an employee.
    Also export the data to a JSON file.
    """
    url = "https://jsonplaceholder.typicode.com"

    # Fetch user information
    user_response = requests.get(f"{url}/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch todos information
    todos_response = requests.get(
        f"{url}/todos", params={'userId': employee_id}
    )
    todos_data = todos_response.json()

    # Calculate the number of completed and total tasks
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get('completed')]
    number_of_done_tasks = len(done_tasks)

    # Prepare data for JSON export
    export_data = {
        str(employee_id): sorted([
            {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": employee_name
            } for task in todos_data
        ], key=lambda x: x['task'])
    }

    # Export data to JSON file
    filename = f"{employee_id}.json"
    with open(filename, 'w') as json_file:
        json.dump(export_data, json_file, indent=2)

    # Display the TODO list progress.
    print(
        f"Employee {employee_name} is done with tasks"
        f"({number_of_done_tasks}/{total_tasks}):"
    )
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            employee_todo_list(employee_id)
        except ValueError:
            print("The employee ID should be an integer.")
