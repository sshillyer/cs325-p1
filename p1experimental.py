#CS 325_400_F2016 Project1 - Correctness Tests
# Jesse Thoren, Shawn Hillyer, Jason Goldfine-Middleton

from analysis_helpers import *
from A1_Enumeration import *
from A2_BetterEnumeration import *
from A3_DivideAndConquer import *
from A4_LinearTime import *
import sys


alg_1_n_values = get_array_of_n_values(10, 5, 20)
print(alg_1_n_values)
for v in alg_1_n_values:
    print(v)