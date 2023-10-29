animals = {"pies", "słoń", "tygrys"}
animals_2 = {"pies","lew","kot"}

print(animals, type(animals))

animals.add("mysz")

print(animals, type(animals))

animals.add("mysz")

print(animals, type(animals))

lista = list(animals)
lista.sort()

animals.remove("mysz")
print(animals, type(animals))
animals.discard("lew")
print(animals, type(animals))

print(animals.update(animals_2))

print(animals, type(animals))