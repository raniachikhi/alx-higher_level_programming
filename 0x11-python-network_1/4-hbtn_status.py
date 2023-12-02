#!/usr/bin/python3
"""
A script that uses the 'requests' library to fetch the status
"""
if __name__ == "__main__":
    from requests import get

    # Send a GET request to the specified URL
    response = get('https://alx-intranet.hbtn.io/status')

    # Display information about the response
    print('Body response:')
    print("\t- type: {}".format(response.text.__class__))
    print("\t- content: {}".format(response.text))
