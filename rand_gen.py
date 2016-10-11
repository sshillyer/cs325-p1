import random

def rand_gen(num_elements = 100):
    '''
    Returns an array of random small integers containing at least one
     positive value.
    '''

    MAX_VALUE = 100
    MIN_VALUE = -100
    at_least_one_positive = False

    while not at_least_one_positive:
        arr = []
        for i in range(num_elements):
            arr.append(random.randint(MIN_VALUE, MAX_VALUE))
            if arr[i] > 0:
                at_least_one_positive = True

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
    arrs.append(rand_gen())

print('Timing algorithm 1 on ten arrays of size 100.')
elapsed_time = time_alg(print, arrs, ITERATIONS)

print('Total time: ' + str(elapsed_time) + ' seconds')
print('Average time: ' + str(elapsed_time / ITERATIONS) + ' seconds')
