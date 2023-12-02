#!/usr/bin/python3
"""
A script that takes a URL and an email, sends a POST request.
"""

if __name__ == "__main__":
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    import sys

    # Get URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the POST request with the provided email parameter
    values = {"email": email}
    request = Request(url, urlencode(values).encode("ascii"))

    # Send the request and display the response body
    with urlopen(request) as response:
        content = response.read().decode('utf-8')
        print(content)
