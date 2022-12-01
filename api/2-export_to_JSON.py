#!/usr/bin/python3
"""
    Fetch data from the corresponding API
    and show the results visually.
    API used: https://jsonplaceholder.typicode.com/
"""
import json
import requests
from sys import argv

if __name__ == '__main__':
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(int(argv[1]))).json()
    tlist = []
    uname = str(user.get('username'))
    uid = str(argv[1])
    for i in tasks:
        tlist.append({
            "task": "{}".format(i.get('title')),
            "completed": i.get('completed'),
            "username": "{}".format(uname)
        })
    jdump = str({"{}".format(uid): tlist})
    with open("{}.csv".format(uid), "w", encoding="UTF-8") as f:
        f.write(jdump)
