#!/usr/bin/python3
"""
6-my_github.py

This script takes your GitHub username and personal access token as arguments, and uses Basic Authentication
with the GitHub API to display your GitHub user ID.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <username> <personal_access_token>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"

    # Create a Basic Authentication header with your username and personal access token
    auth = (username, token)

    response = requests.get(url, auth=auth)

    try:
        data = response.json()
        if 'id' in data:
            print(data['id'])
        else:
            print("None")
    except ValueError:
        print("None")