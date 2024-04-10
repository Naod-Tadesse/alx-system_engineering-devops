#!/usr/bin/python3
"""for a subreddit subs"""
from requests import get


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "PostmanRuntime/7.37.3"}
    response = get(url, headers=headers)
    if response.status_code == 200:
        res = response.json()
        return res["data"]["subscribers"]
    else:
        return 0
