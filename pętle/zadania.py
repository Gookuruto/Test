"""
- Napisz program, który wypisze na ekran wszystkie liczby z przedziału <1000,5000>, są podzielne bez reszty przez 11. (operator %)

- Napisz program, który wczyta od użytkownika wartość liczby naturalnej n. Następnie wypisze na ekran następujący wzorzec o wysokości n linii (przykład dla n = 5):
*
**
***
**
*

-Napisz program, który wczytuje od użytkownika kolejne wartości liczb całkowitych do momentu, gdy ten poda wartość 0.
 Program wypisze wówczas na ekran komunikat ile użytkownik podał liczb parzystych, a ile nieparzystych.
"""
import math


def all_numbers_divisable_by_11():
    numbers = [number for number in range(1000, 5001) if number % 11 == 0]
    numbers_div_by_11 = []
    for number in range(1000, 5001):
        if number % 11 == 0:
            numbers_div_by_11.append(number)
            print(number)
    # for item in range(0,len(numbers),20):
    #     print(numbers[item:item+20])


def print_start():
    n = int(input("podaj liczbe: "))
    half = n//2
    star_multiplier = 1
    if n%2 ==0:
        for number in range(n):
            print("*" * star_multiplier)
            if number < half-1:
                star_multiplier += 1
            elif number >= half:
                star_multiplier -= 1
    else:
        for number in range(n):
            print("*" * star_multiplier)
            if number < half:
                star_multiplier += 1
            else:
                star_multiplier -= 1


# def get_number_from_user():
#     even_numbers_count = 0
#     odd_numbers_count = 0
#     while _____:
#         number = int(input("podaj liczbe: "))
#         if ____:
#             ...
#         if ____:
#             ...
#         else:
#             ...
#     print(f"lisoc liczba parzystych: {even_numbers_count}")
#     print(f"lisoc liczba nieparzystych: {odd_numbers_count}")
