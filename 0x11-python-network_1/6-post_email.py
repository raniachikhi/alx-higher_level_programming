#!/usr/bin/python3
"""
A script that takes a URL and an email address, sends a POST request to the specified URL.
"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]

    response = requests.post(url, data={'email': email})

    print(response.text)
