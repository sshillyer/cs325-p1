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

    # Pass the array from algorithm solution set to the SolutionInstance constructor
    solution = SolutionInstance(input_filename)
    solution.build_solution_from_array(algorithm(graph))

    # Create the file
    solution.write_solution_to_file()

    return



# Returns the vertices in whatever order they are stored in the graph
def crappy_algorithm(graph):
    return graph.V

filename = "provided/tsp_example_1.txt"
execute_tsp_algorithm_from_file(filename, crappy_algorithm)