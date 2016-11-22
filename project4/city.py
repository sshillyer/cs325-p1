from Edge import *

class City(object):
    def __init__(self, label, x, y):
        self.label = label
        self.x = x
        self.y = y
        self.adj = set()

    def __str__(self):
        '''
        Override string method for easy printing of city information
        :return:
        '''
        return str(self.label) + " " + str(self.x) + " " + str(self.y)

    def get_label(self):
        return self.label

    def set_adjacent_city(self, adj_city):
        ''' Untested code '''
        self.adj.add(Edge(self, adj_city))

