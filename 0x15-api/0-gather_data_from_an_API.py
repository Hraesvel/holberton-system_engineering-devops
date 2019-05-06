#!/usr/bin/python3
"""This Script will fetch a user's todo list"""
import requests
import sys

if __name__ == "__main__":
    entrypoint = "https://jsonplaceholder.typicode.com"
    usrId = sys.argv[1]
    try:
        usr = requests.get(
            "{ep}/users/{usrId}".format(ep=entrypoint, usrId=usrId)
        ).json()
        if usr:
            tasks = requests.get(
                "{ep}/todos".format(ep=entrypoint),
                params={"userId": usrId}
            ).json()
            nom_t = len(tasks)
            done_t = [t for t in tasks if t['completed'] is True]
            print(
                "Employee {} is done with tasks({}/{}):"
                .format(usr['name'], len(done_t), nom_t)
            )
            [print('\t ' + t['title']) for t in done_t]
    except Exception as e:
        print(e)
