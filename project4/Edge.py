# UNUSED PRESENTLY

from tsp_helper_functions import *

class Edge(object):
    def __init__(self, u, v):
        self.u = u
        self.v = v
        self.distance = euc_distance(u, v)