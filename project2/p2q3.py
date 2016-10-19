#Jesse Thoren, Shawn Hillyer, Jason Goldfine-Middleton
# Question 3 script

from analysis_helpers2 import *
from changedp import *
from changegreedy import *
from changeslow import *


# 3. Suppose V = [1, 5, 10, 25, 50]. For each integer value of A in [2010, 2015, 2020, …, 2200]
# determine the number of coins that changegreedy and changedp requires. You can attempt to
# run changeslow however if it takes too long you can select smaller values of A and also run the
# other algorithms on the values. Plot the number of coins as a function of A for each algorithm.
# How do the approaches compare?

V = [1, 5, 10, 25, 50]
A = range(2010, 2201, 5)  # start, last+1, step
algorithms = [changegreedy, changedp]
algorithm_labels = ['changegreedy', 'changedp']

for algorithm, label in zip(algorithms, algorithm_labels):
    print(label)

    filename = label + 'q3results.csv'

    # Start a fresh file for the output and print column headers
    f = open(filename, 'w')
    f.write("A,CoinsNeeded\n")
    f.close()

    # run the algorithm on each a value
    for a in A:
        C, m = algorithm(V, a)
        f = open(filename, 'a')
        f.write(str(a) + ',' + str(m) + '\n')
        f.close()

        # Console echo
        print('a: ' + str(a) + '\tm: ' + str(m))
