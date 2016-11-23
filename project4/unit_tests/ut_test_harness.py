from tsp_harness import *

# Returns the vertices in whatever order they are stored in the graph
def crappy_algorithm(graph):
    return graph.V

filename = "../provided/tsp_example_1.txt"
execute_tsp_algorithm_from_file(filename, crappy_algorithm)

# filename = "../provided/tsp_example_2.txt"
# execute_tsp_algorithm_from_file(filename, crappy_algorithm)