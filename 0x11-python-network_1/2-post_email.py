#!/usr/bin/python3
"""
A script that sends a POST request to a URL with an email.
"""
if __name__ == "__main__":
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    from sys import argv

    # Prepare the POST request with the provided email parameter
    values = {"email": argv[2]}
    request = Request(argv[1], urlencode(values).encode("ascii"))

    # Send the request and display the X-Request-Id value and response body
    with urlopen(request) as response:
        x_request_id = response.headers.get('X-Request-Id')
        print(f"X-Request-Id: {x_request_id}")
        print(response.read().decode('utf-8'))
