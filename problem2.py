import json

def search_by_genre(cinema: list, genre: str) -> list:

    natija = []

    for film in cinema:
        if film["genre"] == genre:
            natija.append(film)

    return natija


f = open("cinema.json", "r")

cinema = json.load(f)

f.close()


print(search_by_genre(cinema, "Fantastika"))
print(search_by_genre(cinema, "Drama"))
print(search_by_genre(cinema, "Komediya"))
print(search_by_genre([], "Boevik"))
print(search_by_genre(cinema, "Detektiv"))