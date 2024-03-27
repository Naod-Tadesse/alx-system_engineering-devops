#!/usr/bin/python3
"""get users task progress and export"""
import csv
import requests
import sys


def todo_progress():
    """get the tasks progress and export"""
    url = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]
    response = requests.get(f"{url}/users/{user_id}")

    employee_data = response.json()
    ename = employee_data['name']

    todo_response = requests.get(f"{url}/todos?userId={user_id}")

    todos = todo_response.json()

    tt = len(todos)
    dt = sum(1 for todo in todos if todo['completed'])

    print(f"Employee {ename} is done with tasks ({dt}/{tt}):")
    for todo in todos:
        if todo['completed']:
            print(f"\t{todo['title']}")

    with open(f"{user_id}.csv", 'w', newline='') as csvfile:
        fieldnames = [
            'USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS',
            'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

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
