# An instance /  certificate solution to the TSP
from City import *
from euc_distance import *

class Instance(object):
    def __init__(self, source_filename):
        self.tour_length = 0
        self.num_cities = 0
        self.cities = []
        self.source_filename = source_filename
        self.output_filename = source_filename + '.tour'

    def __str__(self):
        lenString = str(self.tour_length) + '\n'
        cities_string = self.get_cities_string()

        return (lenString + cities_string)

    def add_city_to_tour(self, city):
        self.cities.append(city)

        if self.num_cities > 0:
            last_city = self.cities[self.num_cities-1]  # get the last city in the List
            self.tour_length = self.tour_length + euc_distance(city, last_city)

        self.num_cities = self.num_cities + 1

    def get_cities_string(self):
        cities_string = ''
        for city in self.cities:
            cities_string += str(city.get_label())
            cities_string += '\n'
        return cities_string

    def write_solution_to_file(self):
        with open(self.output_filename, 'w') as out_file:
            out_file.write(self.__str__())