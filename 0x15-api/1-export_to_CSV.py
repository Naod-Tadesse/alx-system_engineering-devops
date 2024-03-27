#!/usr/bin/python3
"""extend your Python script to export data in the CSV format"""
import csv
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    user_response = requests.get("{}/users/{}".format(url, employee_id))
    todos_response = requests.get("{}/todos?userId={}".
                                  format(url, employee_id))

    employee_name = user_response.json().get('username')

    todos = todos_response.json()

    with open("{}.csv".format(employee_id), mode='w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id, employee_name,
                             task['completed'], task['title']])
