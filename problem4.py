import json


def sorted_by_price(products: list) -> list:

    natija = sorted(products, key=lambda x: int(x[1]), reverse=True)

    return natija


f = open("products.json", "r")

products = json.load(f)

f.close()

print(sorted_by_price(products))