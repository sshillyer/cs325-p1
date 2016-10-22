#Jesse Thoren, Shawn Hillyer, Jason Goldfine-Middleton
# Question 4 script
# WARNING: The last part of this runs very slowly on slower machine, if doing more than 1 iteration
# (Like in problem 6 part "5") it would probably take a bit too long to crunch.
from analysis_helpers2 import *
from changedp import *
from changegreedy import *
from changeslow import *

# 5. Suppose V = [1, 2, 4, 6, 8, 10, 12, …, 30]. For each integer value of A in [2000, 2001, 2002, …,
# 2200] determine the number of coins that changegreedy and changedp requires. You can
# attempt to run changeslow however if it takes too long you can select smaller values of A and
# also run all three algorithms on the values. Plot the number of coins as a function of A for each
# algorithm.


def run_q5_test(V_arrays, V_labels, A, algorithms, algorithm_labels, suffix, iterations):
    for V, v_label in zip(V_arrays, V_labels):
        for algorithm, label in zip(algorithms, algorithm_labels):
            print(label + ' ' + v_label)

            filename = 'Q6-Q5' + label + '-' + v_label + suffix + '.csv'

            # Start a fresh file for the output and print column headers
            f = open(filename, 'w')
            f.write("n,Average Runtime\n")
            f.close()

            # run the algorithm on each a value
            for a in A:
                execution_iterations = iterations
                average_runtime = time_alg(algorithm, V, a, execution_iterations)
                f = open(filename, 'a')
                f.write(str(a) + ',' + str(average_runtime) + '\n')
                f.close()

                # Console echo
                print('a: ' + str(a) + '\tAverage Runtime: ' + str(average_runtime))


# Run the test on the faster algorithms on the suggested data set
V = [1]
for i in range(2,31, 2):
    V.append(i)
print(V)

V_arrays = [V]
V_labels = ['v']

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

run_q5_test(V_arrays, V_labels, A, algorithms, algorithm_labels, "-standard", 10)



# Run the test on a smaller range of A
A = range(20, 25, 1)  # start, last+1, step
algorithms = [changegreedy
              , changedp
              ,changeslow
              ]
algorithm_labels = ['changegreedy'
                    ,'changedp'
                    ,'changeslow'
                    ]

run_q5_test(V_arrays, V_labels, A, algorithms, algorithm_labels, "-smallerA", 2)

# EOF
