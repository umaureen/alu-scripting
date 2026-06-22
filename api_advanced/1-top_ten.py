#!/usr/bin/python3
"""Script that fetches 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Print titles of first 10 hot posts for a given subreddit."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            children = data.get('data', {}).get('children', [])
            
            if children:
                for child in children[:10]:
                    print(child.get('data', {}).get('title'))
                return
        except Exception:
            pass
    
    print(None)
