#!/usr/bin/python3
"""This will expand fetch all user and task and organizes the data to
user and task(todos) relationship
"""
if __name__ == "__main__":
    import requests
    import json

    entrypoint = "https://jsonplaceholder.typicode.com"
    try:
        users = requests.get(f"{entrypoint}/users").json()
        tasks = requests.get(f"{entrypoint}/todos").json()

        with open("todo_all_employees.json", "w+") as f:
            collected_tasks = dict()
            for usr in users:
                usr_id = usr["id"]
                usr_task = {usr_id: []}
                for t in [t for t in tasks if t['userId'] == usr_id]:
                    task = dict(
                        username=f'{usr["name"]}',
                        task=f'{t["title"]}',
                        completed=f'{t["completed"]}'
                    )
                    tasks.remove(t)
                    usr_task[usr_id].append(task)
                collected_tasks.update(usr_task)
            json.dump(collected_tasks, f)
    except Exception as e:
        print(e)
