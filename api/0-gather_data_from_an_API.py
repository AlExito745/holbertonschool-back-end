#!/usr/bin/python3
"""Script that return information using REST API."""

import requests
from sys import argv

if __name__ == "__main__":

    if len(argv) > 1:
        usr = argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        req = requests.get("{}users/{}".format(url, usr))
        name = req.json().get("name")
        if name is not None:
            todo = "{}todos?userId={}".format(url, usr)
            jreq = requests.get(todo).json()
            alltsk = len(jreq)
            completedtsk = []
            for t in jreq:
                if t.get("completed") is True:
                    completedtsk.append(t)
            count = len(completedtsk)
            disp = "Employee {} is done with tasks({}/{}):"
            disp = disp.format(name, count, alltsk)
            print(disp)
            for title in completedtsk:
                print("\t {}".format(title.get("title")))