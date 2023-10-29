human = {}

human["name"] = "Maciej"
human["height"] = 180
human["weight"] = 90

print(human)

human_2 = {"name": "Maciej",
           "height": 180.5,
           "weight": 90.5,
           "Hobby": ["Vieo games", "programming", "mountain trips"]
           }
print(human_2)

print(human_2.get("hobby"))

# x = human_2.pop("Hobby")# usuwanie elementu ze slownika v1
del human_2["Hobby"] # usuwanie elementu ze slownika v2
print(human_2)
# print(x)




