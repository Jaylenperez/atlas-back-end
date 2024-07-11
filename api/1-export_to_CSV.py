#!/usr/bin/python3
"""
For a given employee ID,
returns information about his/her TODO list progress.
"""
import csv
import requests
import sys


def export_tasks_to_csv(user_id):
    """
    Export the user's tasks to a CSV file
    """
    url = "https://jsonplaceholder.typicode.com"

    # Fetch user information
    user_response = requests.get(f"{url}/users/{user_id}")
    user_data = user_response.json()
    employee_name = user_data.get('username')

    # Fetch todos information
    todos_response = requests.get(
        f"{url}/todos", params={'userId': user_id}
    )
    todos_data = todos_response.json()

    # Export to CSV.
    with open(f"{user_id}.csv", mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([
                user_id, employee_name,
                task.get('completed'), task.get('title')
            ])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
    else:
        try:
            user_id = int(sys.argv[1])
            export_tasks_to_csv(user_id)
        except ValueError:
            print("The employee ID should be an integer.")
