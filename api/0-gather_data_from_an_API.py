#!/usr/bin/python3
from sys import argv
import json
import requests

emp_ID = int(argv[1])
response = requests.get(f'https://jsonplaceholder.typicode.com/todos/{emp_ID}', verify=False, timeout=10)
print(response.json())