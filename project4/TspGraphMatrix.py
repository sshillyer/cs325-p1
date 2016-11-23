import tsp_helper_functions


class TspGraphMatrix(object):
    def __init__(self, vertices):
        self.V = vertices                   # Vertices (cities)
        self.v_count = n = len(vertices)    # Number of vertices (cities)

        # Initialize and fill in the adjacency matrix
        # See stackoverflow.com/questions/6667201 for initialization line, rest is my logic
        self.AdjMatrix = [[-1 for x in range(n)] for y in range(n)]

        # go through every pair of vertices and calculate the distances, sotring in the AdjMatrix
        for vertex_u in vertices:
            for vertex_v in vertices:
                u = vertex_u.index
                v = vertex_v.index
                self.AdjMatrix[u][v] = tsp_helper_functions.euc_distance(vertex_u, vertex_v)


    def __str__(self):
        return "Graph has " + str(self.v_count) + " vertices"

    def print_matrix(self):
        x, y = 0, 0
        for i in range(self.v_count):
            print (str(i) + '\t')
        for row in self.AdjMatrix:
            print(row)
