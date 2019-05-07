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
        req_user = requests.get(
            "{ep}/users".format(ep=entrypoint),
            params={'id': usrId}
        ).json()
        if req_user:
            req_user = req_user[0]
            req_tasks = requests.get(
                "{ep}/todos".format(ep=entrypoint),
                params={"userId": usrId}
            ).json()
            with open("{}.json".format(usrId), "w+") as f:
                # uId_s = "{}".format(usrId)
                usr_task = {usrId: []}
                for task in req_tasks:
                    t_d = dict(
                        username=req_user["username"],
                        task=task["title"],
                        completed=task["completed"]
                    )
                    usr_task[usrId].append(t_d)
                json.dump(usr_task, f)
    except Exception as e:
        print(e)
