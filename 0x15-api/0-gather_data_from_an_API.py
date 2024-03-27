#!/usr/bin/python3
"""get users task progrsss"""
import requests
import sys


def todo_progress():
    """get the tasks progress"""
    url = "https://jsonplaceholder.typicode.com"
    response = requests.get(f"{url}/users/{sys.argv[1]}")

    employee_data = response.json()
    ename = employee_data['name']

    todo_response = requests.get(f"{url}/todos?userId={sys.argv[1]}")

    todos = todo_response.json()

    tt = len(todos)
    dt = sum(1 for todo in todos if todo['completed'])

    print(f"Employee {ename} is done with tasks ({dt}/{tt}):")

    for todo in todos:
        if todo['completed']:
            print(f"\t{todo['title']}")


if __name__ == "__main__":
    todo_progress()
