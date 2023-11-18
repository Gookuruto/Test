import string
import random

# 85
import timeit

print("zadanie 85")
print("a")
length = random.randint(1, 100)
letters = [string.ascii_letters[random.randint(0, len(string.ascii_letters) - 1)] for i in range(length)]
print("".join(letters))
print("B")
liczba = random.randint(0, 10000)
random_float = random.uniform(0.0, 100.0)
print(liczba)
print(random_float)

print("c")


def f_1():
    liczba = random.randint(0, 70)
    while liczba % 7 != 0:
        liczba = random.randint(0, 70)

    # print(liczba)


def f_2():
    liczba = random.choice(range(0, 71, 7))

    # print(liczba)


print(timeit.timeit(f_1, number=10000))
print(timeit.timeit(f_2, number=10000))

# 86
numbers = [1, 2, 3, 4, 5]
words = ['red', 'black', 'green', 'blue']

print(numbers)
print(words)

#magia
random.shuffle(numbers)
random.shuffle(words)
print(numbers)
print(words)
# 87
# 88
# 89
