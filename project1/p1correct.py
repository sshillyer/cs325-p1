# CS 325_400_F2016 Project1 - Correctness Tests
# Jesse Thoren, Shawn Hillyer, Jason Goldfine-Middleton

from analysis_helpers import *
from A1_Enumeration import *
from A2_BetterEnumeration import *
from A3_DivideAndConquer import *
from A4_LinearTime import *
import sys


def run_algorithm_test(alg, test_arrays, filename):
    results = []
    for test_array in test_arrays:
        result, start, end = alg(test_array)
        write_results_to_file(test_array, start, end, result, filename, 'a')
        results.append(result)
    return results


# File names to read from and write to
if len(sys.argv) == 1:
    in_filename = 'MSS_Problems.txt'
    out_filename = 'MSS_Results.txt'
elif len(sys.argv) == 3:
    in_filename = sys.argv[1]
    out_filename = sys.argv[2]
else:
    print("Usage: p1correct.py [input_file ouput_file]")

print("Reading arrays from: \t" + in_filename)
print("Results saved to:    \t" + out_filename)

# Read the arrays from the specified file
test_arrays = load_arrays_from_file(in_filename)

if not test_arrays:
    print("Could not load file " + in_filename)
    exit()

#out_filename = "MSS_Results.txt"  #TODO Make sure to uncomment this line if using alt file on prior line
border = '=' * 40

results = []

# Run algorithm 1 and append results to filename
write_test_header_to_file(out_filename, 'Algorithm 1: Enumeration', border)
results.append(run_algorithm_test(mss_enumerative, test_arrays, out_filename))

# Run algorithm 2 and append results to filename
write_test_header_to_file(out_filename, 'Algorithm 2: Better Enumeration', border)
results.append(run_algorithm_test(mss_better_enum, test_arrays, out_filename))

# Run algorithm 3 and append results to filename
write_test_header_to_file(out_filename, 'Algorithm 3: Divide & Conquer', border)
results.append(run_algorithm_test(mss_divconq, test_arrays, out_filename))

# Run algorithm 4 and append results to filename
write_test_header_to_file(out_filename, 'Algorithm 4: Linear-Time', border)
results.append(run_algorithm_test(mss_linear, test_arrays, out_filename))

# Log results to console to make sure no discrepencies

for a in results:
    print(a)

# EOF
