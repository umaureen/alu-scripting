#!/usr/bin/python3
"""Script that fetches 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Print titles of first 10 hot posts for a given subreddit."""
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    try:
        data = response.json()
        children = data.get('data', {}).get('children', [])

        if not children:
            print(None)
            return

        for child in children[:10]:
            print(child.get('data', {}).get('title'))

    except Exception:
        print(None)
