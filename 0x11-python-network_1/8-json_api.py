#!/usr/bin/python3
"""
A script that takes a letter and sends a POST request.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    letter = argv[1] if len(argv) > 1 else ""

    response = requests.post('http://0.0.0.0:5000/search_user', data={'q': letter})

    try:
        user_info = response.json()

        if user_info:
            print("[{}] {}".format(user_info.get("id"), user_info.get("name")))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
