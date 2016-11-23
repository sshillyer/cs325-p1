from tsp_harness import *

# Returns the vertices in whatever order they are stored in the graph
def crappy_algorithm(graph):
    return graph.V

def test_execute_tsp(filename, algorithm):
    execute_tsp_algorithm_from_file(filename, algorithm)

test_execute_tsp("../provided/tsp_example_1.txt", crappy_algorithm)
test_execute_tsp("../provided/tsp_example_2.txt", crappy_algorithm)
test_execute_tsp("../provided/tsp_example_3.txt", crappy_algorithm)
