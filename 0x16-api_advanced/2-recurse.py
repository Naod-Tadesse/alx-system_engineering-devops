#!/usr/bin/python3
"""recursively fetch"""
from requests import get
after = None


def recurse(subreddit, hot_list=[]):
    """fetch recursively"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    global after
    agent = {'User-Agent': 'My User custom 2.0'}
    p = {'limit': 100, 'after': after}
    result = get(url, headers=agent, params=p,
                 allow_redirects=False)
    if result.status_code == 200:
        res = result.json()
        dat = res.get('data')
        children = dat.get('children')
        after = dat.get('after')
        for i in children:
            hot_list.append(i.get('data').get('title'))
        if after is not None:
            recurse(subreddit, hot_list)
    else:
        return None
    return hot_list
