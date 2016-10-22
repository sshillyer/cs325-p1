#Jesse Thoren, Shawn Hillyer, Jason Goldfine-Middleton
# Question 6 timing q4 script

from analysis_helpers2 import *
from changedp import *
from changegreedy import *
from changeslow import *

# PART 6: RUNTIME ANALYSIS OF THE FOLLOWING:

# 4. Suppose V1 = [1, 2, 6, 12, 24, 48, 60] and V2 = [1, 6, 13, 37, 150]. For each integer value of A in
# [2000, 2001, 2002, …, 2200] determine the number of coins that changegreedy and changedp
# requires. If your algorithms run too fast try [10,000, 10,001, 10,003, …, 10,100]. You can attempt
# to run changeslow however if it takes too long you can select smaller values of A and also run all
# three algorithms on the values. Plot the number of coins as a function of A for each algorithm.
# How do the approaches compare?

# Note: Compare Q4-changedp-v1-standard.csv to Q4-changegreedy-v1-standard.csv
# Also: Compare Q4-changedp-v2-standard.csv to Q4-changegreedy-v2-standard.csv
# Also: Can compare Q4-*-v{1-2}-smallerA.csv files to one another.

def run_q4_test(V_arrays, V_labels, A, algorithms, algorithm_labels, suffix):
    for V, v_label in zip(V_arrays, V_labels):
        for algorithm, label in zip(algorithms, algorithm_labels):
            print(label + ' ' + v_label)

            filename = 'Q6-Q4' + label + '-' + v_label + suffix + '.csv'

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


# Run the test on the faster algorithms on the suggested data set
V_arrays = [
    [1, 5, 10, 25, 50],  #v1 in description
    [1, 6, 13, 37, 150]  #v2 in description
]
V_labels = ['v1', 'v2']

A = range(4000,7000, 11)  # start, last+1, step
# A = range(10000, 10100, 1)  # blows up changedp algorithm as of 4:46pm 10/19/2016 using v1 array for input
algorithms = [changegreedy
              , changedp
              #,changeslow
              ]
algorithm_labels = ['changegreedy'
                    ,'changedp'
                    #,'changeslow'
                    ]

run_q4_test(V_arrays, V_labels, A, algorithms, algorithm_labels, "-standard")



# Run the test on a smaller range of A
A = range(20, 30, 1)  # start, last+1, step
algorithms = [changegreedy
              , changedp
              ,changeslow
              ]
algorithm_labels = ['changegreedy'
                    ,'changedp'
                    ,'changeslow'
                    ]

run_q4_test(V_arrays, V_labels, A, algorithms, algorithm_labels, "-smallerA")

# EOF
