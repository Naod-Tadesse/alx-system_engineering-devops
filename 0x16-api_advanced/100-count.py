#!/usr/bin/python3
"""count"""
from requests import get

after = None
count_dict = {}
hot_list = []


def count_words(subreddit, word_list):
    """counter"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    agent = {'User-Agent': 'Custom-Agent 2.1.0'}
    global after
    p = {'limit': 100, 'after': after}

    result = get(url, headers=agent, params=p, allow_redirects=False)

    if result.status_code == 200:
        res = result.json()
        dat = res.get('data')
        children = dat.get('children')
        after = dat.get('after')
        for i in children:
            hot_list.append(i['data']['title'])
        for j in hot_list:
            for k in j.lower().split():
                if k in word_list:
                    count_dict[k] = count_dict.get(k, 0) + 1
        if after is not None:
            count_words(subreddit, word_list)
        else:
            sorted_list = sorted(
                count_dict.items(), key=lambda x: (-x[1], x[0]))
            last_occurrence = {}
            for item in sorted_list:
                last_occurrence[item[0]] = item[1]
            for key, value in last_occurrence.items():
                print(f"{key}: {value}")
    else:
        return
