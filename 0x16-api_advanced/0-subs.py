#!/usr/bin/python3
"""for a subreddit subs"""
import requests


def number_of_subscribers(subreddit):
    """sub reddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User-Agent'}
    result = requests.get(url, headers=headers).json()
    try:
        return result['data']['subscribers']
    except Exception:
        return 0
