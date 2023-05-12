#!/usr/bin/python3
"""Nico
This script queries the Reddit API
and returns the number of subscribers
(not active users, total subscribers) for a given subreddit"""
import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    response = requests.get(url, allow_redirects=False, headers={
                            "User-Agent": "Nico@alx/1.0"})
    if response.status_code != 200:
        print(None)
    else:
        data = response.json()
        for child in data['data']['children']:
            print(child['data']['title'])
