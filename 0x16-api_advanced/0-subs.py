#!/usr/bin/python3
"""for a subreddit subs"""
import requests


def number_of_subscribers(subreddit):
    """sub reddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    agent = {'User-Agent': 'PostmanRuntime/7.37.3'}
    result = requests.get(url, headers=agent)
    data = result.json()
    try:
        return data.get('data').get('subscribers')
    except Exception:
        return 0
