#!/usr/bin/python3
"""
A script to send a GET request to a URL specified.
"""
if __name__ == "__main__":
    from requests import get
    from sys import argv

    # Send a GET request to the specified URL
    response = get(argv[1])

    # Display the value of the X-Request-Id variable from the response header
    print(response.headers.get('X-Request-Id'))
