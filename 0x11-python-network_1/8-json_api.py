#!/usr/bin/python3
"""
A script that send a POST request to 'http://0.0.0.0:5000/search_user'.
"""
if __name__ == "__main__":
    from requests import post
    from sys import argv

    search_query = argv[1] if len(argv) > 1 else ""

    response = post('http://0.0.0.0:5000/search_user', data={'q': search_query})

    try:
        user_info = response.json()
        if user_info == {}:
            print('No result')
        else:
            print("[{}] {}".format(user_info.get("id"), user_info.get("name")))
    except ValueError:
        print('Not a valid JSON')
