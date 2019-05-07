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
        req_user = requests.get(
            "{ep}/users/{usrId}".format(ep=entrypoint, usrId=usrId)
        ).json()
        if req_user:
            tasks = requests.get(
                "{ep}/todos".format(ep=entrypoint),
                params={"userId": usrId}
            ).json()
            with open("{usrId}.csv".format(usrId=usrId), "w+") as f:
                fields = ("id", "username", "status", "title")
                writer = csv.DictWriter(
                    f,
                    fieldnames=fields,
                    lineterminator='\n',
                    quotechar='"',
                    quoting=csv.QUOTE_ALL
                )
                for task in tasks:
                    writer.writerow(dict(
                        id=task['userId'],
                        username=req_user["username"],
                        status=task["completed"],
                        title=task["title"]
                    ))
    except Exception as e:
        print(e)
