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
    jdump = {"{}".format(int(argv[1])):
             [{"task": task.get("title"),
               "completed": task.get("completed"),
               "username": user.get('name')} for task in tasks]}
    with open("{}.json".format(int(argv[1])), "w", encoding="UTF-8") as f:
        json.dump(jdump, f)
