from tsp_helper_functions import *
from SolutionInstance import *
from TspGraphMatrix import *

def execute_tsp_algorithm_from_file(input_filename, algorithm):
    '''
    Open the file and run the passed in algorithm
    Build a graph based on the input file
    Run the algorithm to build a solution
    Feed solution into a SolutionInstance
    Output the SolutionInstance using its method

    :param input_filename:
    :param algorithm:
    :return:
    '''

    # read cities from file
    cities = read_city_data_from_file(input_filename)

    # Feed cities into graph and build matrix
    graph = TspGraphMatrix(cities)
    graph.print_matrix()

    # Pass the array from algorithm solution set to the SolutionInstance constructor
    solution = SolutionInstance(input_filename)
    solution_cities = algorithm(graph)
    for city in solution_cities:
        solution.add_city_to_tour(city, graph)

    # Create the file
    solution.write_solution_to_file()

    return

