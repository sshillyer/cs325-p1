#CS 325_400_F2016 Project1 - Correctness Tests
# Jesse Thoren, Shawn Hillyer, Jason Goldfine-Middleton

from analysis_helpers import *
from A1_Enumeration import *
from A2_BetterEnumeration import *
from A3_DivideAndConquer import *
from A4_LinearTime import *
import sys

'''
Set up array of n-values to pass to each algorithm
We set up different sequences to run for each algorithm to ensure we can execute the algorithms within acceptable
time-frames (> ~0 seconds, < ~minute or so)
'''
alg_1_n_values = get_array_of_n_values(10, 10, 20)
alg_2_n_values = get_array_of_n_values(10, 5, 20)
alg_3_n_values = get_array_of_n_values(10, 5, 20)
alg_4_n_values = get_array_of_n_values(10, 5, 20)

# Wrap these up in a single variable
alg_n_values = [alg_1_n_values, alg_2_n_values, alg_3_n_values, alg_4_n_values]
algorithms = [mss_enumerative, mss_better_enum, mss_divconq, mss_linear]


'''
Each call of the algorithm for each n will be executed exactly ITERATIONS times to minimize random variability in
execution times.
'''
ITERATIONS = 10
random.seed()
random.SystemRandom()


for n_values, algorithm in zip(alg_n_values, algorithms):
    for n in n_values:
        arrs = []
        for i in range(ITERATIONS):
            arrs.append(build_random_array(n))

        print('Timing algorithm' )
        elapsed_time = time_alg(algorithm, arrs, ITERATIONS)
#
# print('Total time: ' + str(elapsed_time) + ' seconds')
# print('Average time: ' + str(elapsed_time / ITERATIONS) + ' seconds')
