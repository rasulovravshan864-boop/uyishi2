import json


def are_numbers_ascending(text: str) -> bool:

    sonlar = []

    for i in text.split():
        if i.isdigit():
            sonlar.append(int(i))

    for i in range(len(sonlar) - 1):
        if sonlar[i] >= sonlar[i + 1]:
            return False

    return True


f = open("text.json", "r")

data = json.load(f)

f.close()

for text in data["texts"]:
    print(are_numbers_ascending(text))