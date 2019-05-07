#!/usr/bin/python3
"""This will expand fetch all user and task and organizes the data to
user and task(todos) relationship
"""
import json
import requests
import sys

if __name__ == "__main__":
    entrypoint = "https://jsonplaceholder.typicode.com"
    usrId = sys.argv[1]
    try:
        usr = requests.get(
            "{ep}/users".format(ep=entrypoint),
            params={'id': usrId}
        ).json()
        if usr:
            tasks = requests.get(
                "{ep}/todos".format(ep=entrypoint),
                params={"userId": usrId}
            ).json()
            with open("{}.json".format(usrId), "w+") as f:
                uId_s = "{}".format(usrId)
                usr_task = {uId_s: []}
                for t in tasks:
                    task = dict(
                        username=usr[0]["username"],
                        task=t["title"],
                        completed=t["completed"]
                    )
                    usr_task[uId_s].append(task)
                json.dump(usr_task, f)
    except Exception as e:
        print(e)
