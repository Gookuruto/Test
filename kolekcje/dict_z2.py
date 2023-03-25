"""
stworz słownik ktory kazdej postaci przypisze film z którego pochodzi. A następnie wypisz postacie tylko z jednego filmu.
"""

postaci = ["R2D2", "C3P0", "Yoda", "Harry Potter", "Iron Man", "Kapitan Ameryka", "Spider-man", "Darth Vader",
           "Han Solo",
           "Hermiona Granger", "Ron Weasley", "Albus Dumbledore"]

filmy = ["Star Wars", "Harry Potter", "Avangers"]

char_movie = [("R2D2", "Star Wars"), ("C3P0", "Star Wars"), ("Yoda", "Star Wars"), ("Harry Potter", "Harry Potter"),
              ("Iron Man", "Avangers"), ("Kapitan Ameryka", "Avangers"), ("Spider-man", "Avangers"),
              ("Darth Vader", "Star Wars"),
              ("Han Solo", "Star Wars"),
              ("Hermiona Granger", "Harry Potter"), ("Ron Weasley", "Harry Potter"),
              ("Albus Dumbledore", "Harry Potter")]

slownik_1 = {postac: film for (postac, film) in char_movie}

slownik_2 = {}
for movie in filmy:
    slownik_2[movie.lower()] = []

for (character, movie) in char_movie:
    slownik_2[movie.lower()].append(character)
print(slownik_2)

movie = input("podaj film (Star Wars, Harry Potter, Avangers)")
# print(slownik_2[movie.lower()])
# for character in slownik_2[movie.lower()]:
#     print(character, end=", ")
for key, value in slownik_1.items():
    if str(value).lower() == movie.lower():
        print(key)

# Wyswietl postacie z filmu movie
