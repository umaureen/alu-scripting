#!/usr/bin/python3
"""Script that fetches 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Print titles of first 10 hot posts for a given subreddit."""
    
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    # Use www.reddit.com and add limit parameter
    subreddit_url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    
    # Don't follow redirects to avoid redirecting to search results
    response = requests.get(subreddit_url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        json_data = response.json()
        children = json_data.get('data', {}).get('children', [])
        
        # Check if we got any posts
        if not children:
            print(None)
            return
            
        for child in children[:10]:  # Ensure we only get first 10
            print(child.get('data', {}).get('title'))
    else:
        print(None)
