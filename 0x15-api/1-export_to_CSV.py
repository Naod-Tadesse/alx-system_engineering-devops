#!/usr/bin/python3
"""csv format"""
import csv
import requests
import sys


def getcsv():
    """get csv"""
    url = "https://jsonplaceholder.typicode.com"
    uresponse = requests.get(f"{url}/users/{sys.argv[1]}")
    tresponse = requests.get(f"{url}/todos?userId={sys.argv[1]}")

    jsson = uresponse.json()
    ename = jsson.get('username')

    todos = tresponse.json()

    with open(f"{sys.argv[1]}.csv", mode='w') as filecsv:
        file = csv.writer(filecsv, quoting=csv.QUOTE_ALL)
        for todo in todos:
            file.writerow(
                [sys.argv[1], ename, todo['completed'], todo['title']])


if __name__ == "__main__":
    getcsv()
