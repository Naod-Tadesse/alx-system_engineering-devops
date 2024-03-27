#!/usr/bin/python3
"""json export"""
import json
import requests
import sys


def todo_progress():
    """json export"""
    url = "https://jsonplaceholder.typicode.com"
    response = requests.get(f"{url}/users/{sys.argv[1]}")

    ename = response.json()['username']

    tr = requests.get(f"{url}/todos?userId={sys.argv[1]}")

    todos = tr.json()

    tasks_arr = []
    for todo in todos:
        tasks_arr.append({
            "task": todo["title"],
            "completed": todo["completed"],
            "username": ename
        })

    with open(f"{sys.argv[1]}.json", 'w') as file:
        json.dump({sys.argv[1]: tasks_arr}, file)


if __name__ == "__main__":
    todo_progress()
