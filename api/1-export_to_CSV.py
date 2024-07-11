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
    employee_name = user_data.get('name')

    # Fetch todos information
    todos_response = requests.get(
        f"{url}/todos", params={'userId': user_id}
    )
    todos_data = todos_response.json()

    # Calculate the number of completed and total tasks
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get('completed')]
    number_of_done_tasks = len(done_tasks)

    # Display the TODO list progress.
    print(
        f"Employee {employee_name} is done with tasks"
        f"({number_of_done_tasks}/{total_tasks}):"
    )
    for task in done_tasks:
        print(f"\t {task.get('title')}")

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
