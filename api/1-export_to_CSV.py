#!/usr/bin/python3
"""
    Fetch data from the corresponding API
    and show the results visually.
    API used: https://jsonplaceholder.typicode.com/
"""
import requests
from sys import argv
import pandas as pd

if __name__ == '__main__':
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(int(argv[1]))).json()
    tlst = []
    for i in tasks:
        if i.get('userId') == int(argv[1]):
            tlst.append({'UID': argv[1], 'Uname': user.get('username'),
                 'status': i.get('completed'), 'title': i.get('title')})
    df = pd.DataFrame(tlst)
    df.to_csv('USER_ID.csv', index=False, header=False)
