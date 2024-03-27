#!/usr/bin/python3
"""get users task progrsss"""
import requests
import sys


def todo_progress():
    """get the tasks progress"""
    url = "https://jsonplaceholder.typicode.com"
    response = requests.get(f"{url}/users/{sys.argv[1]}")

    employee_data = response.json()
    employee_name = employee_data['name']

    todo_response = requests.get(f"{url}/todos?userId={sys.argv[1]}")

    todos = todo_response.json()

    total_tasks = len(todos)
    done_tasks = sum(1 for todo in todos if todo['completed'])

    print(
        f"Employee {employee_name} is done with \
tasks({done_tasks}/{total_tasks}):")
    for todo in todos:
        if todo['completed']:
            print(f"\t{todo['title']}")


if __name__ == "__main__":
    todo_progress()
