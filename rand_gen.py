#CS 325_400_F2016 Project1 - Algo4: Linear Time
# Jesse Thoren, Shawn Hillyer, Jason Goldfine-Middleton

import random

def build_random_array(num_elements = 100):
    '''
    Returns an array of random small integers containing at least one
     positive value.
    '''

    MAX_VALUE = 100
    MIN_VALUE = -100
    at_least_one_positive = False


    arr = []
    for i in range(num_elements):
        arr.append(random.randint(MIN_VALUE, MAX_VALUE))
        if arr[i] > 0:
                at_least_one_positive = True

    if not at_least_one_positive:
        random_index = random.randint(0, num_elements - 1)
        arr[random_index] = abs(arr[random_index])

    return arr


def time_alg(alg, arr, cycles):
    '''
    Executes an algorithm's execution _cycles_ times and returns the
     elapsed time, in seconds.
    '''
    import timeit

    elapsed_time = 0

    for i in range(cycles):
        start = timeit.default_timer()
        alg(arr[i])
        stop = timeit.default_timer()
        elapsed_time += stop - start

    return elapsed_time

ITERATIONS = 10
#random.seed()
random.SystemRandom()
arrs = []
for i in range(ITERATIONS):
    arrs.append(build_random_array())

print('Timing algorithm 1 on ten arrays of size 100.')
elapsed_time = time_alg(print, arrs, ITERATIONS)

print('Total time: ' + str(elapsed_time) + ' seconds')
print('Average time: ' + str(elapsed_time / ITERATIONS) + ' seconds')
