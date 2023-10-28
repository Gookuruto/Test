import sys
import random as rng
from math import sqrt
args = sys.argv
print(args)
print("Dzielenie")
try:
    x = int(args[1])

    y = int(args[2])

    print(x/y)
except ZeroDivisionError:
    print("Prosze nie dzielic przez 0")
except ValueError:
    print("Prosze podawac tylko liczby")
finally:
    print("Konczymy program.")