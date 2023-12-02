#!/usr/bin/python3
"""
A script that uses the 'requests' library to send a POST request to a URL specified.
"""
if __name__ == "__main__":
    from requests import post
    from sys import argv

    # Send a POST request to the specified URL with the provided email parameter
    response = post(argv[1], data={'email': argv[2]})

    # Display the body of the response
    print(response.text)
