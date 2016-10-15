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

TODO: Adjust these values so that we get higher time values and a smoother looking plot
'''
# Call arguments: (Starting Value, Increment Between Values, Quantity of n to test (Minimum is 10) )
alg_1_n_values = get_array_of_n_values(10, 10, 25)
alg_2_n_values = get_array_of_n_values(10, 50, 25)
alg_3_n_values = get_array_of_n_values(10, 1000, 25)
alg_4_n_values = get_array_of_n_values(10, 2500, 25)

# Wrap these up in a single variable
alg_n_values = [alg_1_n_values, alg_2_n_values, alg_3_n_values, alg_4_n_values]
algorithms = [mss_enumerative, mss_better_enum, mss_divconq, mss_linear]
labels = ["Enumeration", "BetterEnumeration", "DivideAndConquer", "Linear"]

'''
Each call of the algorithm for each n will be executed exactly ITERATIONS times to minimize random variability in
execution times.
'''
ITERATIONS = 20
random.SystemRandom()

for n_values, algorithm, label in zip(alg_n_values, algorithms, labels):
    print('Timing algorithm: ' + label)

    # Open results file for appending, insert header
    filename = label + '-results.csv'
    f = open(filename, 'w')
    f.write("n,average time\n")

    # Run the test for each size n in alg_*_n_values[] array
    for n in n_values:
        arrs = []

        # Build i arrays of size n
        for i in range(ITERATIONS):
            arrs.append(build_random_array(n))

        # Pass each algorithm and its corresponding arrays in to the timer
        print('n=' + str(n))
        elapsed_time = time_alg(algorithm, arrs, ITERATIONS)
        average_time = elapsed_time / ITERATIONS

        # Write the algorithm's average run time for current n to a csv file
        f.write(str(n) + ',' + str(average_time) + '\n')

        # Echo results to console for easy debugging
        print('Total time: ' + str(elapsed_time) + ' seconds')
        print('Average time: ' + str(average_time) + ' seconds')

    f.write('\n')
    f.close()