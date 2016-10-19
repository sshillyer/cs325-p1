# Testing for correctness. Above all else your algorithm should be correct. You can test your algorithms
# on the following:

# 2. Suppose V = [1, 3, 7, 12] and A = 29. The changegreedy should return C = [2, 1, 0, 2] with m = 5
# and changedp and slowchange should return C = [0, 1, 2, 1] with m = 4. The minimum number of coins
# is four. The greedy algorithm is suboptimal.
# 3. If A is changed above to 31, all algorithms should return C = [0, 0, 1, 2], with m = 3.

from analysis_helpers2 import *

from changedp import *
from changegreedy import *
from changeslow import *

algorithms = [changedp, changegreedy, changeslow]
algorithm_lables = ["changedp()", "changegreed()", "changeslow"]

# 1. Suppose V = [1, 2, 4, 8] and A = 15. All algorithms should return C=[1,1,1,1] and m = 4.
V = [1, 2, 4, 8]
A = 15
C_expected = [1, 1, 1, 1]
m_expected = 4

for algorithm, label in zip(algorithms, algorithm_lables):
    C, m = algorithm(V, A)
    print('Testing algorithm ' + label)
    print('input: ' + str(V) + ', ' + str(A))
    print('output: ' + str(C) + ', ' + str(m))
    print('expect: ' + str(C_expected) + ', ' + str(m_expected))
    if C != C_expected or m != m_expected:
        print("OH SNAP we have a problem")
