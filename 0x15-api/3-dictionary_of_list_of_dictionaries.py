#!/usr/bin/python3
"""data export"""
import json
import requests
import sys


def alltasks():
    """data export"""
    url = "https://jsonplaceholder.typicode.com"

    uresponse = requests.get(f"{url}/users")
    udata = uresponse.json()

    tasks = {}

    for user in udata:
        user_id = str(user["id"])
        username = user["username"]

        tasks_response = requests.get(f"{url}/todos?userId={user_id}")
        tasks_data = tasks_response.json()

        utasks = []
        for task in tasks_data:
            utasks.append({
                "username": username,
                "task": task["title"],
                "completed": task["completed"]})

        tasks[user_id] = utasks

    with open("todo_all_employees.json", 'w') as file:
        json.dump(tasks, file)


if __name__ == "__main__":
    alltasks()
