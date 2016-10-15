# CS 325 Algorithms - Project 1
## Group Members:
* Jesse Thoren
* Shawn Hillyer
* Jason Goldfine-Middleton

### Description
This code base implements several versions of the Maximum Sum Subarray algorithm.

The file p1correct.py is used to execute a script written in Python3 that runs a series of tests by reading in a 
series of arrays from an input file, then executing the algorithm and using the return values to print the original
array, the "MSS" array, and the sum of that subarray with labels for clarity.

The file p1experimental.py will execute automated tests to four files, *-results.csv, which can easily be imported to
a spreadsheet program compatible with comma-separated-value format files. This is intended for use in plotting the run-
time results 

The algorithms are in the A*_*.py files and are based on the project descriptions algorithms.

The file analysis_helpers.py includes several helper functions used to generate random arrays, print results to file,
and time the execution of algorithms passed in, etc.

### Usage

#### Correctness Testing
Execute p1correct.py using python3. By default, it will read in the arrays MSS_Problems.txt and output
 will be written to MSS_Results.txt. Results will be appended to the file. 

Usage:  python3 p1correct.py

#### Experimental Testing
Execute p1experimental.py using python3. To fun custom tests of varying n-values or iterations, you will need to
modify the source code. This code could easily be modified to test other algorithms in the future.

Usage: python3 p1algorithm.py