#Used in primsMST

from tsp_helper_functions import *

class Edge(object):
    def __init__(self, u, v, *distance):
        self.u = u
        self.v = v
        if distance:
            self.distance = distance[0]
        else:
            self.distance = euc_distance(u,v)
