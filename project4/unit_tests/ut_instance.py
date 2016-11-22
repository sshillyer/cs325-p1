from Instance import *
from City import *

sol = Instance('tsp_example_1.txt')
print(sol)

city1 = City(1,5,10)
city2 = City(2,10,10)
city3 = City(3, 15, 30)
sol.add_city_to_tour(city1)
print(sol)
# expect length of 0 and the one city
sol.add_city_to_tour(city2)
print(sol)
sol.add_city_to_tour(city3)
print(sol)

sol.write_solution_to_file()