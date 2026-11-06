import json


def majority_element(nums: list) -> int:

    if len(nums) == 0:
        return -1

    sonlar = {}

    for i in nums:
        if i in sonlar:
            sonlar[i] += 1
        else:
            sonlar[i] = 1

    max_son = 0
    natija = -1

    for i in sonlar:
        if sonlar[i] > max_son:
            max_son = sonlar[i]
            natija = i

    return natija


f = open("numbers.json", "r")

data = json.load(f)

f.close()

nums = data["nums"]

print(majority_element(nums))