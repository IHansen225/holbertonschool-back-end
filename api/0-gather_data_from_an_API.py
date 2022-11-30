#!/usr/bin/python3
""" Get data from API server """
from sys import argv
import requests


emp_ID = int(argv[1])
tasks = requests.get("https://jsonplaceholder.typicode.com/todos",
                    timeout=10).json()
user = requests.get(f"https://jsonplaceholder.typicode.com/users/{emp_ID}",
                    timeout=10).json()
completed_tasks_list = [i for i in tasks if i['completed']
                        is True and i['userId'] == emp_ID]
total_tasks = len([i for i in tasks if i['userId'] == emp_ID])
print(f"Employee {user['name']} is done with tasks\
({len(completed_tasks_list)}/{total_tasks}):")
for i in completed_tasks_list:
    print("\t" + i['title'])
