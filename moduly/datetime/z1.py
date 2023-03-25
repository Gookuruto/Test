"""
Zamien podany string na obiekt typu datetime np.
wejscie:
    date_string = "Feb 25 2020 4:20PM"
wyjscie:
    2020-02-25 16:20:00

dokumentacja:
https://docs.python.org/3/library/datetime.html?highlight=strptime#datetime.datetime.strptime
"""

from datetime import datetime

date_string = "Feb 25 2020 4:20PM"

datetime_object = datetime.strptime(date_string, "%b %d %Y %I:%M%p")

print(type(datetime_object))
print(datetime_object)