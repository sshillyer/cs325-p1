
#CS 325_400_F2016 Project1 - Algo1: Enumeration
# Jesse Thoren, Shawn Hillyer, Jason Goldfine-Middleton

from analysis_helpers import *
from A1_Enumeration import *
from A2_BetterEnumeration import *
from A3_DivideAndConquer import *
from A4_LinearTime import *


def run_algorithm_test(alg, test_arrays, expected_results, filename):
    for test_array, expected in zip(test_arrays, expected_results):
        result, start, end = alg(test_array)
        print("test_array: " + str(result) + ".\t Expected: " + str(expected))
        print("Start index: " + str(start) + "\tEnd Index: " + str(end))
        write_results_to_file(test_array, start, end, result, filename, "a")


# TODO: Read in the arrays from file; this is just a small sample

test_arrays = [
    [1, 4, -9, 8, 1, 3, 3, 1, -1, -4, -6, 2, 8, 19, -10, -11]
    , [2, 9, 8, 6, 5, -11, 9, -11, 7, 5, -1, -8, -3, 7 -2]
    , [10, -11, -1, -9, 33, -45, 23, 24, -1, -7 -8, 19]
    ]
expected_results = [34, 30, 50]

filename = "test.txt"

# Run algorithm 1 and append results to filename
run_algorithm_test(mss_enumerative, test_arrays, expected_results, filename)

# Run algorithm 2 and append results to filename
run_algorithm_test(mss_better_enum, test_arrays, expected_results, filename)

# Run algorithm 3 and append results to filename
run_algorithm_test(mss_divconq, test_arrays, expected_results, filename)

# Run algorithm 4 and append results to filename
run_algorithm_test(mss_better_enum, test_arrays, expected_results, filename)



# # Algorithm 2: Better Enumeration
# def mssBetterEnumeration(a):
#     n = len(a)
#
#     # Return values
#     bestSum = -99999999                 # stores the highest MSS found so far
#     bestSumStartIndex = 0       # stores the index of the starting element of the current best MSS
#     bestSumEndIndex = 0         # stores the index of the last element of the current best MSS
#
#     # Enumerating nested loops to calculate best sums so far
#     for i in range(0, n):       # start at each element in the array and calculate all sums
#         priorSum = 0
#         for j in range (i, n):  # Calculate the sum from i to j, for j = i to end of array
#             sumCandidate = priorSum + a[j]
#             priorSum = sumCandidate
#
#             if sumCandidate > bestSum:
#                 bestSum = sumCandidate
#                 bestSumStartIndex = i
#                 bestSumEndIndex = j
#
#     return bestSum, bestSumStartIndex, bestSumEndIndex




# Run test on each of the values in the array of inputs
# for v in testValuesRecur:
#     start = timeit.default_timer()
#
#     for i in range(numTests):
#         recursiveFib(v)
#
#     stop = timeit.default_timer()
#     totalTime = stop - start
#     averageTime = totalTime / numTests
#     print(str(v) + "," + str(averageTime))
#
#     f.write(str(v) + "," + str(averageTime) + "\n")
# f.close()


#
#
# test_array = [1, 4, -9, 8, 1, 3, 3, 1, -1, -4, -6, 2, 8, 19, -10, -11]
# expected = 34
# result, start, end = mssEnumerative(test_array)
# print("test_array: " + str(result) + ".\t Expected: " + str(expected))
# print("Start index: " + str(start) + "\tEnd Index: " + str(end))
# writeMssTestToFile(test_array, start, end, result)
#
#
# test_array = [2, 9, 8, 6, 5, -11, 9, -11, 7, 5, -1, -8, -3, 7 -2]
# expected = 30
# result, start, end = mssEnumerative(test_array)
# print("test_array: " + str(result) + ".\t Expected: " + str(expected))
# print("Start index: " + str(start) + "\tEnd Index: " + str(end))
#
# test_array = [10, -11, -1, -9, 33, -45, 23, 24, -1, -7 -8, 19]
# expected = 50
# result, start, end = mssEnumerative(test_array)
# print("test_array: " + str(result) + ".\t Expected: " + str(expected))
# print("Start index: " + str(start) + "\tEnd Index: " + str(end))
#
# test_array = [31,-41, 59, 26, -53, 58, 97, -93, -23, 84]
# expected = 187
# result, start, end = mssEnumerative(test_array)
# print("test_array: " + str(result) + ".\t Expected: " + str(expected))
# print("Start index: " + str(start) + "\tEnd Index: " + str(end))
#
# test_array = [3, 2, 1, 1, -8, 1, 1, 2, 3]
# expected = 7
# result, start, end = mssEnumerative(test_array)
# print("test_array: " + str(result) + ".\t Expected: " + str(expected))
# print("Start index: " + str(start) + "\tEnd Index: " + str(end))
#
#
# test_array = [12, 99, 99, -99, -27, 0, 0, 0, -3, 10]
# expected = 210
# result, start, end = mssEnumerative(test_array)
# print("test_array: " + str(result) + ".\t Expected: " + str(expected))
# print("Start index: " + str(start) + "\tEnd Index: " + str(end))
#
#
# test_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# expected = 6
# result, start, end = mssEnumerative(test_array)
# print("test_array: " + str(result) + ".\t Expected: " + str(expected))
# print("Start index: " + str(start) + "\tEnd Index: " + str(end))
#
#
#
#
# # Testing the better enumeration algorithm 2
# test_array = [1, 4, -9, 8, 1, 3, 3, 1, -1, -4, -6, 2, 8, 19, -10, -11]
# expected = 34
# result, start, end = mssBetterEnumeration(test_array)
# print("test_array: " + str(result) + ".\t Expected: " + str(expected))
# print("Start index: " + str(start) + "\tEnd Index: " + str(end))
#
# test_array = [2, 9, 8, 6, 5, -11, 9, -11, 7, 5, -1, -8, -3, 7 -2]
# expected = 30
# result, start, end = mssBetterEnumeration(test_array)
# print("test_array: " + str(result) + ".\t Expected: " + str(expected))
# print("Start index: " + str(start) + "\tEnd Index: " + str(end))
#
# test_array = [10, -11, -1, -9, 33, -45, 23, 24, -1, -7 -8, 19]
# expected = 50
# result, start, end = mssBetterEnumeration(test_array)
# print("test_array: " + str(result) + ".\t Expected: " + str(expected))
# print("Start index: " + str(start) + "\tEnd Index: " + str(end))
#
# test_array = [31,-41, 59, 26, -53, 58, 97, -93, -23, 84]
# expected = 187
# result, start, end = mssBetterEnumeration(test_array)
# print("test_array: " + str(result) + ".\t Expected: " + str(expected))
# print("Start index: " + str(start) + "\tEnd Index: " + str(end))
#
# test_array = [3, 2, 1, 1, -8, 1, 1, 2, 3]
# expected = 7
# result, start, end = mssBetterEnumeration(test_array)
# print("test_array: " + str(result) + ".\t Expected: " + str(expected))
# print("Start index: " + str(start) + "\tEnd Index: " + str(end))
#
#
# test_array = [12, 99, 99, -99, -27, 0, 0, 0, -3, 10]
# expected = 210
# result, start, end = mssBetterEnumeration(test_array)
# print("test_array: " + str(result) + ".\t Expected: " + str(expected))
# print("Start index: " + str(start) + "\tEnd Index: " + str(end))
#
#
# test_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# expected = 6
# result, start, end = mssBetterEnumeration(test_array)
# print("test_array: " + str(result) + ".\t Expected: " + str(expected))
# print("Start index: " + str(start) + "\tEnd Index: " + str(end))