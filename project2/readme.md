# CS 325 Algorithms - Project 2
## Group Members:
* Jesse Thoren
* Shawn Hillyer
* Jason Goldfine-Middleton

### Description
This code implements several algorithms for the Coin Change problem:
* analysis_helpers2.py is slightly tweaked version of our project 1 helper function file. Very few functions were used.
* changedp.py is the Dynamic Programming version of the algorithm. This includes only the function def.
* changegreedy.py is the Greedy algorithm. Includes only the function def.
* changeslow.py is the Slow algorithm. Only the function def.
* p2correct.py is the script used to verify our algorithms properly execute
* p2q*.py files are used to verify and automatically run tests for questions 3, 4, 5, 6, and 7; each generates .csv file

### Usage

#### Correctness Testing
Execute p2correct.py using python3. There are no command line arguments. Visual inspection shows correctness, but
scrypt will print out an error message if there's a difference between the actual and expected return values.

Usage:  python3 p2correct.py

#### Experimental Testing
Executing a script may take some time as we collected large sample sizes for most problem sets (several minutes+)

Usage: python3 p2q3.py
Usage: python3 p2q4.py
Usage: python3 p2q5.py
Usage: python3 p2q6timingq3.py
Usage: python3 p2q6timingq4.py
Usage: python3 p2q6timingq5.py
Usage: python3 p2q7.py


Some of the scripts generate multiple csv files. The -standard and -smaller suffix are designating the size of A.
In particular, the -smallerA.csv files include the slow algorithm results on small size A.