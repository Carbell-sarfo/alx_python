#!/usr/bin/python3
"""
0-hbtn_status.py

This script makes an HTTP GET request to https://alu-intranet.hbtn.io/status using the 'requests' library.
It then displays information about the response, including its type and content.
"""

import requests

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)

    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))