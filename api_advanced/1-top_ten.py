#!/usr/bin/python3
"""Script that fetch 10 hot post for a given subreddit."""
import requests


def top_ten(subreddit):
    """Print titles of first 10 hot posts for a given subreddit."""
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(subreddit_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        json_data = response.json()
        children = json_data.get('data', {}).get('children', [])
        
        if children:
            for i in range(min(10, len(children))):
                print(children[i].get('data', {}).get('title'))
        else:
            print(None)
    else:
        print(None)
