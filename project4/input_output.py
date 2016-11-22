from City import *


# Read data from an input file and store into a list of City objects
def read_city_data_from_file(filename):
    # Open file for reading and read in each line
    with open(filename, 'r') as data_file:
        lines = data_file.readlines()

    cities = []

    # Unpack each line to variables and instantiate the city, adding it to the cities array
    for line in lines:
        label, x, y = line.split()
        city = City(label, x, y)
        cities.append(city)

    # Return a list of cities with label, x, y  all set from reading filename
    return cities

