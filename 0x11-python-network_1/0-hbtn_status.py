#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status."""

from urllib import request, error

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    try:
        with request.urlopen(url) as page:
            content = page.read()
            print("Body response:")
            print("\t- type: {}".format(type(content)))
            print("\t- content: {}".format(content))
            print("\t- utf8 content: {}".format(content.decode('utf-8')))
    except error.URLError as e:
        print("Error: {}".format(e.reason))
