from city import *
from euc_distance import *

# Simple function to test that we get the correct result
def test_euc(x1, y1, x2, y2, expected):
    city1 = City(1, x1, y1)
    city2 = City(2, x2, y2)
    distance = euc_distance(city1, city2)
    print("Expect\t" + str(expected) + "\tActual:\t" + str(distance))
    if (distance != expected):
        print("Unit test failed for call: (" + x1 + ", " + y1 + ", " + x2 + ", " + y2 + ", " + expected + ")")
        return False
    else:
        return True

# Write test cases here
# Using www.calculatorsoup.com/calculators/geometry-plane/distance-two-points.php to get expected answer (round to nearest!)
test_euc(5, 10, 100, 22, 96)
test_euc(22, 396, 55, 984, 589)
test_euc(5646,654, 54,0,5630)