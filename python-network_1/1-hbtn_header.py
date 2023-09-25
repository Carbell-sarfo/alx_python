#!/usr/bin/python3
"""
1-hbtn_header.py

This script takes a URL as an argument, sends a GET request to the URL using the 'requests' library,
and displays the value of the 'X-Request-Id' header in the response.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    response = requests.get(url)

    # Check if the 'X-Request-Id' header is present in the response
    if 'X-Request-Id' in response.headers:
        print(response.headers['X-Request-Id'])
    else:
        print("Header 'X-Request-Id' not found in the HTTP header.")
        sys.exit(1)