#!/usr/bin/python3
"""This will expand on task 0 and convert the data
to a CSV
"""
if __name__ == "__main__":
    import requests
    import sys
    import csv

    entrypoint = "https://jsonplaceholder.typicode.com"
    usrId = sys.argv[1]
    try:
        usr = requests.get(
            "{ep}/users/{usrId}".format(ep=entrypoint, usrId=usrId)
        ).json()
        tasks = requests.get(
            "{ep}/todos".format(ep=entrypoint),
            params={"userId": usrId}
        ).json()
        nom_t = len(tasks)
        done_t = [t for t in tasks if t['completed'] is True]

        with open("{usrId}.csv".format(usrId=usrId), "w+") as f:
            fields = ("id", "username", "status", "title")
            writer = csv.DictWriter(f, fieldnames=fields, lineterminator='\n')
            for task in tasks:
                writer.writerow(dict(
                    id=task['userId'],
                    username=usr["name"],
                    status=task["completed"],
                    title=task["title"]
                ))
    except Exception as e:
        print(e)
