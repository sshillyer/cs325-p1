# Testing for correctness. Above all else your algorithm should be correct. You can test your algorithms
# on the following:

from analysis_helpers2 import *

from changedp import *
from changegreedy import *
from changeslow import *

def run_tests(V, A, algorithms, algorithm_labels, C_expecteds, m_expecteds):
    '''
    Runs tests on a set of algorithms and compares the expected and actual results
    :param algorithms: array of n algorithms
    :param algorithm_labels:  array of n strings to represent the algorithms
    :param C_expecteds:  array of n arrays of expected return value for C
    :param m_expecteds: array of expected return values for m
    :return: none
    '''
    for algorithm, label, C_expected, m_expected in zip(algorithms, algorithm_labels, C_expecteds, m_expecteds):
        C, m = algorithm(V, A)
        print('Testing algorithm ' + label)
        print('input: ' + str(V) + ', ' + str(A))
        print('output: ' + str(C) + ', ' + str(m))
        print('expect: ' + str(C_expected) + ', ' + str(m_expected))
        if C != C_expected or m != m_expected:
            print("OH SNAP we have a problem")

# Testing same 3 algorithms and labels each time
algorithms = [changedp, changegreedy, changeslow]
algorithm_lables = ["changedp()", "changegreedy()", "changeslow"]


# 1. Suppose V = [1, 2, 4, 8] and A = 15. All algorithms should return C=[1,1,1,1] and m = 4.
V = [1, 2, 4, 8]
A = 15
C_expecteds = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    ]
m_expecteds = [4, 4, 4]

run_tests(V, A, algorithms, algorithm_lables, C_expecteds, m_expecteds)

# 2. Suppose V = [1, 3, 7, 12] and A = 29. The changegreedy should return C = [2, 1, 0, 2] with m = 5
# and changedp and slowchange should return C = [0, 1, 2, 1] with m = 4. The minimum number of coins
# is four. The greedy algorithm is suboptimal.

# algorithms = [changedp, changegreedy, changeslow]
V = [1, 3, 7, 12]
A = 29
C_expecteds = [
    [0, 1, 2, 1], #changedp
    [2, 1, 0, 2], #changegreedy
    [0, 1, 2, 1], #changeslow
    ]
m_expecteds = [4, #changedp
               5, #changegreedy
               4] #changeslow

run_tests(V, A, algorithms, algorithm_lables, C_expecteds, m_expecteds)

# 3. If A is changed above to 31, all algorithms should return C = [0, 0, 1, 2], with m = 3.
V = [1, 3, 7, 12]
A = 31
C_expecteds = [
    [0, 0, 1, 2], #changedp
    [0, 0, 1, 2], #changegreedy
    [0, 0, 1, 2], #changeslow
    ]
m_expecteds = [3, #changedp
               3, #changegreedy
               3] #changeslow

run_tests(V, A, algorithms, algorithm_lables, C_expecteds, m_expecteds)