#!/usr/bin/python3
"""for a subreddit subs"""
import requests


def number_of_subscribers(subreddit):
    """sub reddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'PostmanRuntime/7.37.3'}
    result = requests.get(url, headers=headers).json()
    try:
        return result.get('data').get('subscribers')
    except Exception:
        return 0
