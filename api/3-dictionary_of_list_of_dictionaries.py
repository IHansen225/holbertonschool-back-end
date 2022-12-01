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
    user = requests.get("https://jsonplaceholder.typicode.com/users/").json()
    all_dump = dict()
    for u in user:
        tlst = [{"task": t.get('title'),
                 "completed": t.get('completed'),
                 "username": u.get('username')} for t in tasks if t.get('userId') == u.get('id')]
        all_dump["{}".format(u.get('id'))] = tlst
    with open("todo_all_employees.json", "w", encoding="UTF-8") as f:
        json.dump(all_dump, f)
