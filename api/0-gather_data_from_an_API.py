#!/usr/bin/python3
"""
Fetch data from the corresponding API
and show the results visually.
API used: https://jsonplaceholder.typicode.com/
"""
import requests
from sys import argv

if __name__ == '__main__':
    emp_ID = int(argv[1])
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos",
                         timeout=10).json()
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(emp_ID),
                        timeout=10).json()
    completed_tasks_list = [i for i in tasks if i.get('completed') and
                            i.get('userId') == emp_ID]
    total_tasks = len([i for i in tasks if i['userId'] == emp_ID])
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'),
                  len(completed_tasks_list),
                  total_tasks))
    for i in completed_tasks_list:
        print("\t {}".format(i.get('title')))
