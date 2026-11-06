import json


def merge_unique_ids(active_users: list, new_users: list) -> list:

    natija = []

    for i in active_users:
        if i not in natija:
            natija.append(i)

    for i in new_users:
        if i not in natija:
            natija.append(i)

    return natija


f = open("users.json", "r")

data = json.load(f)

f.close()

active_users = data["active_users"]
new_users = data["new_users"]

print(merge_unique_ids(active_users, new_users))