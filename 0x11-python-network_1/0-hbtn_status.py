#!/usr/bin/python3
"""
Fetches the status and displays information about the response.
"""

if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()
        print("Body response:")
        print("\t- Type: {}".format(type(content)))
        print("\t- Content: {}".format(content))
        print("\t- UTF-8 Content: {}".format(content.decode('utf-8')))
