#!/usr/bin/python3
"""top ten"""
import requests


def top_ten(subreddit):
    """top ten"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "PostmanRuntime/7.37.3"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            for post in data['data']['children']:
                print(post['data']['title'])
        else:
            print("None")
    except Exception as e:
        print("None")
