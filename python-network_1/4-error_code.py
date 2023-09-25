#!/usr/bin/python3
"""
4-error_code.py

This script takes a URL as an argument, sends an HTTP request to the URL using the 'requests' library,
and displays the body of the response. If the HTTP status code is greater than or equal to 400,
it prints an error message with the status code.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    response = requests.get(url)

    print(response.text)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))