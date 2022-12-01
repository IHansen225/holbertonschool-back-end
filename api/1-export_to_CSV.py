#!/usr/bin/python3
"""
    Fetch data from the corresponding API
    and show the results visually.
    API used: https://jsonplaceholder.typicode.com/
"""
import requests
from sys import argv

if __name__ == '__main__':
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(int(argv[1]))).json()
    csvs = ""
    uname = user.get('username')
    uid = str(argv[1])
    for i in tasks:
        if i.get('userId') == int(argv[1]):
            csvs += ("{}, {}, {}, {}\n"
            .format(uid, uname, i.get('completed'), i.get('title')))
    print(csvs)
