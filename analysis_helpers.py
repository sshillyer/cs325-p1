#CS 325_400_F2016 Project1 - Analysis Helpers
# Jesse Thoren, Shawn Hillyer, Jason Goldfine-Middleton

import random


def load_arrays_from_file(filename):
    '''
    Parses a text file for integer arrays and returns them as a list
        of lists of integers.
    :param filename: absolute or relative path to the input file
    :return: a list containing lists of integers
    '''
    with open(filename, 'r') as array_file:
        contents = array_file.read()

    contents = (contents.strip()            # strip whitespace at ends
                        .replace('[', '')   # replace useless characters
                        .replace(']', '')
                        .replace(' ', '')   # replace whitespace
                        .split('\n'))       # separate the lines   

    arrays = []
    for line in contents:
        # split line into tokens at each comma and convert tokens to numbers
        arrays.append([int(num) for num in line.split(',')])

    return arrays


def write_results_to_file(a, mss_first, mss_last, result, filename ='test', 
        write_mode ='w'):
    '''
    Writes original array and the subarray from mss_first to mss_last
        with labels. Appends if write_mode is "a", otherwise overwrites file
    :param a: array of integers
    :param mss_first: index of start of the maximum sum subarray
    :param mss_last: index of start of the maximum sum subarray
    :param result: The sum of the mss
    :param filename: File name to output results
    :param write_mode: the file write mode to use ("a" = append, etc.,
                       same as file.open() arg2)
    :return:
    '''
    n = len(a)
    f = open(filename, write_mode)

    # Write original array to file
    f.write('Original Array:\n')
    write_array_to_file(f, a, 0, n)

    # Write the MSS array to the file
    f.write('Maximum Sum Subarray:\n')
    write_array_to_file(f, a, mss_first, mss_last + 1)

    # Write result to the file
    f.write('Maxiumum Sum:\n')
    f.write(str(result) + '\n\n')

    f.close()


def write_array_to_file(f, a, m, n):
    '''
    Writes a[m..n] to file f with an opening and closing [ ], comma-delimited.
    :param f: filename to write to
    :param a: array to read values from
    :param m: index of starting element of array
    :param n: index of last element of array
    :return:
    '''
    f.write('[')
    for i in range(m, n - 1):
        f.write(str(a[i]))
        f.write(', ')
    f.write(str(a[n - 1]))
    f.write(']\n')



def write_test_header_to_file(filename, label, border):
    '''
    Writes a header to an ASCII file.
    :param filename: File to write to
    :param label: ASCII text to write
    :param border: Border to print; if null, won't print
    :return:
    '''
    f = open(filename, 'a')
    if border:
        f.write(border + '\n')
    f.write(label + '\n')
    if border:
        f.write(border + '\n')
    f.write('\n')
    f.close()



def build_random_array(size = 100):
    '''
    Returns an array of random small integers.
    :param size: size of array
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
    Executes an algorithm's execution 'cycles' times and returns the
        elapsed time, in seconds.
    :param alg: function to time
    :param arr: array to pass to alg
    :param cycles: number of times to execute the function
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

def get_array_of_n_values(first, step_size, qty):
    '''
    Return an array of values starting at value first, incrementing by step_size, consisting of exactly qty elements
    Note: THis is used to generate the various values of 'n' to pass to the algorithms
    :param first: Value of the first element of the array
    :param step_size: Value to increment by for each value
    :param qty: Number of values to generate
    :return: Array of values array[start, start+step_size, start+step_size*2, start+step_size+3, .., start+step_size*qty]
    '''
    last = first + (qty * step_size)
    array = range(first, last, step_size)
    return array



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
