# CS 325_400_F2016 Project1 - Analysis Helpers
# Jesse Thoren, Shawn Hillyer, Jason Goldfine-Middleton

# Quick script to crunch the numbers for Part 5 of the Experimental Analysis

from math import *

def algorithm_1(n):
    # t = 2E-08x3 - 3E-06x2 + 0.0004x - 0.0098
    return (.00000002 * (n ** 3)) - (.000003 * (n ** 2)) + (.0004 * n) - (.0098)

def algorithm_2(n):
    # t = 7E-08x2 + 2E-06x - 0.0011
    return ((.00000007 * (n ** 2)) + (0.000002 * n) - 0.011)

def algorithm_3(n):
    # 4E-06x - 0.0001=10
    return (.000004 * n - 0.001)

def algorithm_4(n):
    # 2E-07x - 3E-05
    return (.0000002 * n - .00003)

def check_solution(solutions, algorithm, label):
    for n in solutions:
        print(str(label) + ' n = ' + str(n) + '\tRuntime = ' + str(algorithm(n)))
        print(str(label) + ' n = ' + str(floor(n)) + '\t\tRuntime = ' + str(algorithm(floor(n))))
        print(str(label) + ' n = ' + str(ceil(n)) + '\t\tRuntime = ' + str(algorithm(ceil(n))))

a1_solutions = [838.5, 1191.5, 1489.5]
check_solution(a1_solutions, algorithm_1, 'Alg 1')

a2_solutions = [11944.7, 20691.1, 29265.5]
check_solution(a2_solutions, algorithm_2, 'Alg 2')


a3_solutions = [2500100, 7500025, 15000025]
check_solution(a3_solutions, algorithm_3, 'Alg 3')

a4_solutions = [50000150, 150000150, 300000150]
check_solution(a4_solutions, algorithm_4, 'Alg 4')
