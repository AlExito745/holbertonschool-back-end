#!/usr/bin/python3
"""Script that export data in CSV format."""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    uid = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(uid)
    usr = requests.get(url, verify=False).json()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}"
    url = url.format(uid)
    todo = requests.get(url, verify=False).json()
    with open("{}.csv".format(uid), 'w', newline='') as csvfile:
        tskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for t in todo:
            result = [int(uid), usr.get("username")]
            result += [t.get("completed"), t.get("title")]
            tskwriter.writerow(result)
