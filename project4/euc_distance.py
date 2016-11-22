from City import *
from math import sqrt

# function to return the distance between two points on Euclidian plain
# accepts to City objects and calculates the distance between them
def euc_distance(c1, c2):
    # d(c1, c2) = nearest_int(squareroot((x1-x2)^*2 + (y1-y2)**2))
    x1, x2, y1, y2 = c1.x, c2.x, c1.y, c2.y

    return int(round(sqrt((x1-x2)**2 + (y1-y2)**2)))

    return unrounded_result



