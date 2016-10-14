#CS 325_400_F2016 Project1 - Correctness Tests
# Jesse Thoren, Shawn Hillyer, Jason Goldfine-Middleton

from analysis_helpers import *
from A1_Enumeration import *
from A2_BetterEnumeration import *
from A3_DivideAndConquer import *
from A4_LinearTime import *
import sys

def set_n_values(start, step_size, qty):
    start = start
    step = step_size
    qty = qty
    stop = start + (qty * step)
    return start, stop, step

start, stop, step = set_n_values(10, 5, 20)
alg_1_n_values = range(start, stop, step)

print(alg_1_n_values)
for v in alg_1_n_values:
    print(v)