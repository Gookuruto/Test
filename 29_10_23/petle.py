# # n = 0
# #
# # while True:
# #     n -= 1
# #     if n == 4:
# #         break
# #     if n == 1:
# #         continue
# #     print(n)
# # print("koniec petli")
#
# animals = ["Dog", "Cat", "Fish"]
# animal_food = ["Dog food", "cat food", "fish food"]
# for index, animal in enumerate(animals):
#     print(animal, index)
#     if animal == "Dog":
#         animal_food[index] = "Premium Dog food"
#
# print(animals)
# print(animal_food)
#
# # for number in range(100, -1, -1):
# #     print(number)

print("Zadanie 57:")
counter = 100
total = 0
while counter >0:
    total += counter
    counter -=1
print(counter)
print(total)
