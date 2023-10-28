class City:
    def __init__(self, name, lat_d, lat_m, lat_s, lon_d, lon_m, lon_s):
        self.name = name
        self.lat_d = lat_d
        self.lat_m = lat_m
        self.lat_s = lat_s
        self.lon_d = lon_d
        self.lon_m = lon_m
        self.lon_s = lon_s

    def get_lat_and_lon(self):
        latitude = self.lat_d + (self.lat_m / 60) + (self.lat_s / 3600)
        longitude = self.lon_d + (self.lon_m / 60) + (self.lon_s / 3600)

        return latitude, longitude

    def __repr__(self):
        return f"Miasto: {self.name} ma współrzędne {self.get_lat_and_lon()}"


def read_cities(path):
    cities_list = []
    with open(path, "r") as data:
        first_line = data.readline()
        for line in data:
            splited_data = line.split(",")
            if len(splited_data)<8:
                break
            city = City(splited_data[8], float(splited_data[0]), float(splited_data[1]), float(splited_data[2]), float(splited_data[4]),
                        float(splited_data[5]), float(splited_data[6]))
            cities_list.append(city)

    return cities_list

#
# cities = read_cities("cities.csv")
#
# print(cities)

import csv

csv_file = open("cities.csv","r")

reader = csv.reader(csv_file,delimiter=",")
cities_list = []
for splited_data in list(reader)[1:]:
    if len(splited_data) <8:
        continue
    city = City(splited_data[8], float(splited_data[0]), float(splited_data[1]), float(splited_data[2]),
                float(splited_data[4]),
                float(splited_data[5]), float(splited_data[6]))
    cities_list.append(city)
csv_file.close()
print(cities_list)

import pandas as pd

cities = pd.read_csv("cities.csv")

print(cities.values)