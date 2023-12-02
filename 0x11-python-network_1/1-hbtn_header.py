#!/usr/bin/python3
"""
Fetches a URL specified as an argument and displays the value.
"""
if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)
