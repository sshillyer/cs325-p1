#CS 325_400_F2016 Project1 - Algo4: Linear Time
# Jesse Thoren, Shawn Hillyer, Jason Goldfine-Middleton

import random


def write_results_to_file(a, mss_first, mss_last, result, filename ="test", write_mode ="w"):
    '''
    Writes original array and the subarray from mss_first to mss_last
        with labels. Appends if write_mode is "a", otherwise overwrites file
    :param a: array of integers
    :param mss_first: index of start of the maximum sum subbary
    :param mss_last: index of start of the maximum sum subbary
    :param result: The sum of the mss
    :param filename: FIle name to output results
    :param write_mode: The file write mode to use ("a" = append, etc., same as file.open() arg2
    :return:
    '''
    n = len(a)
    f = open(filename, write_mode)

    # Write original array to file
    f.write("Original Array:\n")
    write_array(f, a, 0, n)

    # Write the MSS array to the file
    f.write("Maximum Sum Subarray:\n")
    write_array(f, a, mss_first, mss_last)

    # Write result to the file
    f.write("Maxiumum Sum:\n")
    f.write(str(result) + "\n\n")

    f.close()



def write_array(f, a, m, n):
    '''
    writes a[m..n] to file f with an opening and closing [ ], comma delimited
    :param f: filename to write to
    :param a: array to read values from
    :param m: index of starting element of array
    :param n: index of last element of array
    :return:
    '''
    f.write("[")
    for i in range(m, n - 1):
        f.write(str(a[i]))
        f.write(", ")
    f.write(str(a[n - 1]))
    f.write("]\n")


def build_random_array(size = 100):
    '''
    Returns an array of random small integers
    :param size: Size of array
    :return:
    '''
    MAX_VALUE = 100
    MIN_VALUE = -100
    at_least_one_positive = False


    arr = []
    for i in range(size):
        arr.append(random.randint(MIN_VALUE, MAX_VALUE))
        if arr[i] > 0:
                at_least_one_positive = True

    if not at_least_one_positive:
        random_index = random.randint(0, size - 1)
        arr[random_index] = abs(arr[random_index])

    return arr


def time_alg(alg, arr, cycles):
    '''
    Executes an algorithm's execution _cycles_ times and returns the
        elapsed time, in seconds.
    :param alg: Function to time
    :param arr: Array to pass to alg
    :param cycles: Number of times to execute the function
    :return:
    '''
    import timeit

    elapsed_time = 0

    for i in range(cycles):
        start = timeit.default_timer()
        alg(arr[i])
        stop = timeit.default_timer()
        elapsed_time += stop - start

    return elapsed_time

# ITERATIONS = 10
# #random.seed()
# random.SystemRandom()
# arrs = []
# for i in range(ITERATIONS):
#     arrs.append(build_random_array())
#
# print('Timing algorithm 1 on ten arrays of size 100.')
# elapsed_time = time_alg(print, arrs, ITERATIONS)
#
# print('Total time: ' + str(elapsed_time) + ' seconds')
# print('Average time: ' + str(elapsed_time / ITERATIONS) + ' seconds')
