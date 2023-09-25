#!/usr/bin/python3
"""
5-json_api.py

This script takes a letter as an argument, sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter, and displays the result based on the JSON response.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        letter = ""
    else:
        letter = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': letter}

    response = requests.post(url, data=payload)

    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")