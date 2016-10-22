#Jesse Thoren, Shawn Hillyer, Jason Goldfine-Middleton
# Question 4 script
# WARNING: The last part of this runs very slowly on slower machine, if doing more than 1 iteration
# (Like in problem 6 part "5") it would probably take a bit too long to crunch.
from analysis_helpers2 import *
from changedp import *
from changegreedy import *
from changeslow import *

def run_q7_test(V_arrays, V_labels, A, algorithms, algorithm_labels, suffix, iterations):
    for V, v_label in zip(V_arrays, V_labels):
        for algorithm, label in zip(algorithms, algorithm_labels):
            print(label + ' ' + v_label)

            filename = 'Q7' + '-' + v_label + suffix + '.csv'

            # Start a fresh file for the output and print column headers
            f = open(filename, 'w')
            f.write("A,Average Runtime,n\n")
            f.close()

            # run the algorithm on each a value
            for a in A:
                execution_iterations = iterations
                average_runtime = time_alg(algorithm, V, a, execution_iterations)
                f = open(filename, 'a')
                f.write(str(a) + ',' + str(average_runtime) + ',' + str(len(V)) + '\n')
                f.close()

                # Console echo
                print(str(a) + ',' + str(average_runtime) + ',' + str(len(V)) + '\n')


# Run the test on the faster algorithms on the suggested data set

V = [1]
for i in range(2,31, 2):
    V.append(i)

V2 = [1]
for i in range(2,100, 3):
    V2.append(i)

V3 = [1]
for i in range(2,500, 7):
    V3.append(i)

V_arrays = [
    [1, 5, 10, 25, 50], # 5
    [1, 6, 13, 37, 150], # 5
    [1, 2, 6, 12, 24, 48, 60],  #7
    V,
    V2,
    V3
]

V_labels = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6']

A = [75, 176, 517]
# A = range(10000, 10100, 1)  # blows up changedp algorithm as of 4:46pm 10/19/2016 using v1 array for input
algorithms = [changegreedy
              , changedp
              ]
algorithm_labels = ['changegreedy'
                    ,'changedp'
                    ]

run_q7_test(V_arrays, V_labels, A, algorithms, algorithm_labels, "", 10)

# EOF
