from City import *


# Read data from an input file and store into a list of City objects
def read_city_data_from_file(filename):
    with open(filename, 'r') as data_file:
        lines = data_file.readlines()

    cities = []

    for line in lines:
        # print(line)
        label, x, y = line.split()
        city = City(label, x, y)
        cities.append(city)

    return cities

