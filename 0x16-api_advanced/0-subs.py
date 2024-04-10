#!/usr/bin/python3
"""for a subreddit subs"""
import requests


def number_of_subscribers(subreddit):
    """sub reddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    agent = {'User-Agent': 'PostmanRuntime/7.37.3'}
    result = requests.get(url, headers=agent)
    if result.status_code == 200:
        res = result.json()
        return res.get('data').get('subscribers')
    else:
        return 0
