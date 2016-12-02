Students:	Jesse Thoren, Shawn Hillyer, Jason Goldfine-Middleton
CS325-400: 	Project 4 

========================================================================
readme.txt
========================================================================

----------------------------------------
Usage
----------------------------------------
To generate our best (time-unbounded) solutions, execute the following
command(s):

*
*
*

TO generate our competition solutions, execute the following commands:

*
*
*


----------------------------------------
File Descriptions
----------------------------------------
/bestSolutions/
	Contains the best solutions obtained for the tsp_example_{1-3}.txt
	inputs and the test-input-{1-7}.txt inputs without a time limit.

/bestSolutionsCompetition/
	Contains the best solutions obtained for the test-input-{1-7}.txt 
	inputs as calculated in <= 3 minutes.

/unit_tests/
	Unit tests for some of the functions we wrote

/   (ROOT)
	The Root directory contains the rest of the functions we used.

	City.py
		Class that stores the label, index, and x/y coordinates for
		cities; simplies algorithms.

	primsRefactor.py
		TODO

	primsSubmissionTest7.py
		TODO

	primsSubmissionTests1to6.py
		TODO

	tsp_helper_functions.py
		Functions to read the city data from a file, build the Graph,
		and calculate the Euclidian Distance between two City objects

	TspGraphMatrix.py
		Class to encapsulate the Graph using a set of Vertices and 
		an Adjacency Matrix and get distance between vertices in constant
		time (once calculated and stored in the table)



----------------------------------------
TSP Verifier Commands
----------------------------------------

The TSP Verifier (tsp-verifier.py) and TPSAllVisisted.py and watch.py
files are in our two solutions files for easy testing. You can copy-paste
the commands below to verify the solutions.

(For both folders)
python tsp-verifier.py test-input-1.txt test-input-1.txt.tour
python tsp-verifier.py test-input-2.txt test-input-2.txt.tour
python tsp-verifier.py test-input-3.txt test-input-3.txt.tour
python tsp-verifier.py test-input-4.txt test-input-4.txt.tour
python tsp-verifier.py test-input-5.txt test-input-5.txt.tour
python tsp-verifier.py test-input-6.txt test-input-6.txt.tour
python tsp-verifier.py test-input-7.txt test-input-7.txt.tour

(For the bestSolutions folder only)
python tsp-verifier.py tsp_example_1.txt tsp_example_1.txt.tour
python tsp-verifier.py tsp_example_2.txt tsp_example_2.txt.tour
python tsp-verifier.py tsp_example_3.txt tsp_example_3.txt.tour