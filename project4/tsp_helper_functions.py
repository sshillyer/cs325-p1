from TspGraphMatrix import *
from City import *
from math import sqrt

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

def build_graph_from_file(filename):
    # Read the cities into an array by parsing filename
    cities = read_city_data_from_file(filename)

    # Pass the cities into the TspGraphMatrix constructor
    graph = TspGraphMatrix(cities)

    return graph


# function to return the distance between two points on Euclidian plain
# accepts to City objects and calculates the distance between them
def euc_distance(c1, c2):
    # d(c1, c2) = nearest_int(squareroot((x1-x2)^*2 + (y1-y2)**2))
    x1, x2, y1, y2 = c1.x, c2.x, c1.y, c2.y

    return int(round(sqrt((x1-x2)**2 + (y1-y2)**2)))

    return unrounded_result