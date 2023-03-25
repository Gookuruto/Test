"""
Napisz program który przetasuje elementy z danej listy.
"""
import random

numbers = [1, 2, 3, 4, 5]
words = ['red', 'black', 'green', 'blue']

print(numbers)
print(words)

print("Shuffle")
random.shuffle(numbers)
random.shuffle(words)

print(numbers)
print(words)