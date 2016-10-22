#Jesse Thoren, Shawn Hillyer, Jason Goldfine-Middleton
# Question 6 analysze question 3 timing script

from analysis_helpers2 import *
from changedp import *
from changegreedy import *
from changeslow import *

# PART 6: RUNTIME ANALYSIS OF THE FOLLOWING:

# 3. Suppose V = [1, 5, 10, 25, 50]. For each integer value of A in [2010, 2015, 2020, …, 2200]
# determine the number of coins that changegreedy and changedp requires. You can attempt to
# run changeslow however if it takes too long you can select smaller values of A and also run the
# other algorithms on the values. Plot the number of coins as a function of A for each algorithm.
# How do the approaches compare?

V = [1, 5, 10, 25, 50]
A = range(4000, 7100, 33)  # start, last+1, step
algorithms = [changegreedy, changedp]
algorithm_labels = ['changegreedy', 'changedp']

for algorithm, label in zip(algorithms, algorithm_labels):
    print(label)

    filename = 'Q6-Q3' + label + '.csv'

    # Start a fresh file for the output and print column headers
    f = open(filename, 'w')
    f.write("n,Average Runtime\n")
    f.close()

    # run the algorithm on each a value
    for a in A:
        execution_iterations = 10
        average_runtime = time_alg(algorithm, V, a, execution_iterations)
        f = open(filename, 'a')
        f.write(str(a) + ',' + str(average_runtime) + '\n')
        f.close()

        # Console echo
        print('a: ' + str(a) + '\tAverage Runtime: ' + str(average_runtime))

# EOF
