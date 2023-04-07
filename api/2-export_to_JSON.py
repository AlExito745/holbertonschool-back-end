#!/usr/bin/python3
"""Script that export data in JSON format."""

import json
import requests
from sys import argv

if __name__ == "__main__":
    uid = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(uid)
    usr = requests.get(url, verify=False).json()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}"
    url = url.format(uid)
    todo = requests.get(url, verify=False).json()
    name = usr.get("username")
    result = [{"task": result.get("title"), "username": name}]
    result += [{"completed": result.get("completed")} for result in todo]
    kj = {}
    kj[uid] = result
    with open("{}.json".format(uid), 'w') as filejs:
        json.dump(kj, filejs)
