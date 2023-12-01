#!/usr/bin/python3
"""
A simple script that fetches the status of https://alx-intranet.hbtn.io and displays information about the response.
Usage:
    $ python3 script_name.py
"""

if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()
        print("Body response:")
        print("\t- Type: {}".format(type(content)))
        print("\t- Content: {}".format(content))
        print("\t- UTF-8 Content: {}".format(content.decode('utf-8')))
