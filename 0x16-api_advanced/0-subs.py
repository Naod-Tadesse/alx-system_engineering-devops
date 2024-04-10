#!/usr/bin/python3
"""subreddit"""
import requests


def number_of_subscribers(subreddit):
    """
    no of subs
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyCoolScript/1.0 (by /u/naod)"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json()
            return data["data"]["subscribers"]
        except (KeyError, json.JSONDecodeError):
            return 0
    else:
        return 0
