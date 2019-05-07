#!/usr/bin/python3
"""This will expand fetch all user and task and organizes the data to
user and task(todos) relationship
"""
if __name__ == "__main__":
    import json
    import requests

    entrypoint = "https://jsonplaceholder.typicode.com"
    try:
        users = requests.get("{}/users".format(entrypoint)).json()
        tasks = requests.get("{}/todos".format(entrypoint)).json()

        with open("todo_all_employees.json", "w+") as f:
            collected_tasks = dict()
            for usr in users:
                usr_id = usr["id"]
                usr_task = {usr_id: []}
                for t in [t for t in tasks if t['userId'] == usr_id]:
                    task = dict(
                        username=usr["username"],
                        task=t["title"],
                        completed=t["completed"]
                    )
                    tasks.remove(t)
                    usr_task[usr_id].append(task)
                collected_tasks.update(usr_task)
            json.dump(collected_tasks, f)
    except Exception as e:
        print(e)
