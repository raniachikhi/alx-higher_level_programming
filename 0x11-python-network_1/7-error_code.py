#!/usr/bin/python3
"""
A script that send a GET request to a URL specified as a command-line argument.
"""
if __name__ == "__main__":
    from requests import get
    from sys import argv

    response = get(argv[1])

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
