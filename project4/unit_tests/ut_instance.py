from SolutionInstance import *
from tsp_helper_functions import *

sol = SolutionInstance('tsp_example_1.txt')
cities = read_city_data_from_file("../provided/tsp_example_1.txt")

for city in cities:
    sol.add_city_to_tour(city)

sol.write_solution_to_file()
