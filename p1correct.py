#CS 325_400_F2016 Project1 - Correctness Tests
# Jesse Thoren, Shawn Hillyer, Jason Goldfine-Middleton

from analysis_helpers import *
from A1_Enumeration import *
from A2_BetterEnumeration import *
from A3_DivideAndConquer import *
from A4_LinearTime import *
import sys


def run_algorithm_test(alg, test_arrays, filename):
    for test_array in test_arrays:
        result, start, end = alg(test_array)
        write_results_to_file(test_array, start, end, result, filename, 'a')

# These arrays are hard coded from the file
# test_arrays = [
#     [1, 4, -9, 8, 1, 3, 3, 1, -1, -4, -6, 2, 8, 19, -10, -11]
#     , [2, 9, 8, 6, 5, -11, 9, -11, 7, 5, -1, -8, -3, 7 -2]
#     , [10, -11, -1, -9, 33, -45, 23, 24, -1, -7 -8, 19]
#     , [31,-41, 59, 26, -53, 58, 97, -93, -23, 84]
#     , [3, 2, 1, 1, -8, 1, 1, 2, 3]
#     , [12, 99, 99, -99, -27, 0, 0, 0, -3, 10]
#     , [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#     ]

# File names to read from and write to
if len(sys.argv) == 1:
    in_filename = 'MSS_Problems.txt'
    out_filename = 'MSS_Results.txt'
elif len(sys.argv) == 3:
    in_filename = sys.argv[1]
    out_filename = sys.argv[2]
else:
    print("Usage: p1correct.py [input_file] [ouput_file]")

print("Reading arrays from: \t" + in_filename)
print("Results saved to:    \t" + out_filename)

# Read the arrays from the specified file
test_arrays = load_arrays_from_file(in_filename)

if not test_arrays:
    print("Could not load file " + in_filename)
    exit()

#out_filename = "MSS_Results.txt"  #TODO Make sure to uncomment this line if using alt file on prior line
border = '=' * 40

# Run algorithm 1 and append results to filename
write_test_header_to_file(out_filename, 'Algorithm 1: Enumeration', border)
run_algorithm_test(mss_enumerative, test_arrays, out_filename)

# Run algorithm 2 and append results to filename
write_test_header_to_file(out_filename, 'Algorithm 2: Better Enumeration', border)
run_algorithm_test(mss_better_enum, test_arrays, out_filename)

# Run algorithm 3 and append results to filename
write_test_header_to_file(out_filename, 'Algorithm 3: Divide & Conquer', border)
run_algorithm_test(mss_divconq, test_arrays, out_filename)

# Run algorithm 4 and append results to filename
write_test_header_to_file(out_filename, 'Algorithm 4: Linear-Time', border)
run_algorithm_test(mss_linear, test_arrays, out_filename)

# EOF
