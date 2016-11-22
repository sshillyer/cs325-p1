from input_output import *

# test read_city_data_from_file
def test_read_city_data_from_file(filepath):
    city_data = read_city_data_from_file(filepath)

    print("Displaying city data as read from " + filepath)
    print("label x y")
    for city in city_data:
        print(city)


test_read_city_data_from_file("../provided/tsp_example_1.txt")
test_read_city_data_from_file("../provided/tsp_example_2.txt")
test_read_city_data_from_file("../provided/tsp_example_3.txt")