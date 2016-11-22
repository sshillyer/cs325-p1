from input_output import *


# read_city_data_from_file
city_data = read_city_data_from_file("../provided/tsp_example_1.txt")

for city in city_data:
    print(city)