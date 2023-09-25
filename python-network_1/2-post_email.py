#!/usr/bin/python3
"""
2-post_email.py

This script takes a URL and an email address as arguments, sends a POST request to the URL
with the email as a parameter, and displays the body of the response.
"""

import requests
import sys
from urllib.parse import urlencode

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email parameter and append it to the URL
    encoded_email = urlencode({'email': email})
    url_with_email = f"{url}?{encoded_email}"

    response = requests.post(url_with_email)

    print("Your email is: {}".format(email))
    print(response.text)