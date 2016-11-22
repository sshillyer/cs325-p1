from City import *
from euc_distance import *
from Edge import *

class TspGraphAdj(object):
    def __init__(self):
        self.V = []         # Vertices, aka, cities
        self.v_count = 0    # Number of vertices

    def add_vertex(self, city):
        # Add the city to the graph
        self.V.append(city)

        '''
        Calculate the distance from new city to every existing city, storing the distance
        on both the new city (distance from new to existing) AND on the existing (from existing to new)
        '''

        for existing_city in self.V:
            existing_city.set_adjacent_city(city)
            city.set_adjacent_city(existing_city)
