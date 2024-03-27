#!/usr/bin/python3
"""get users task progress and export to CSV"""
import requests
import csv
import sys


def todo_progress():
    """get the tasks progress and export to CSV"""
    url = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]
    response = requests.get(f"{url}/users/{user_id}")

    employee_data = response.json()
    ename = employee_data['name']

    todo_response = requests.get(f"{url}/todos?userId={user_id}")

    todos = todo_response.json()

    tt = len(todos)
    dt = sum(1 for todo in todos if todo['completed'])

    with open(f"{user_id}.csv", 'w', newline='') as csvfile:
        fieldnames = [
            'USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS',
            'TASK_TITLE']
        writer = csv.DictWriter(
            csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)

        writer.writeheader()
        for todo in todos:
            writer.writerow({
                'USER_ID': user_id,
                'USERNAME': ename,
                'TASK_COMPLETED_STATUS': todo['completed'],
                'TASK_TITLE': todo['title']
            })


if __name__ == "__main__":
    todo_progress()
