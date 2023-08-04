import random
import string
from datetime import datetime, timedelta


# 85
def zad_85a(n: int):
    alfa_sekwencja = ""
    for i in range(n):
        alfa_sekwencja += random.choice(string.ascii_letters)
    return alfa_sekwencja


def zad_85b(a: int, b: int):
    return random.randint(a, b)


# print(zad_85b(1,100))

def zad_85c():
    lst = [i for i in range(0, 70, 7)]
    return random.choice(lst)


def zad_85c_op2():
    while True:
        liczba = random.randint(0, 70)
        if liczba % 7 == 0:
            return liczba


# 87

def zad_87():
    rng_val = [random.randint(0, 100000000000) for i in range(100)]
    return random.sample(rng_val, 10)


# 88
def zad_88():
    date_string = "Feb 25 2020 4:20 PM"
    datetime_object = datetime.strptime(date_string, "%b %d %Y %I:%M %p")
    return datetime_object


# result = zad_88()
# print(type(result))
# print(result)

# 89

given_date = datetime(2020, 2, 25)
print(given_date)
days_to_substract = 7
time_to_substract = timedelta(days=days_to_substract)
res_date = given_date - time_to_substract
print(res_date)
