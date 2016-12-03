Students:	Jesse Thoren, Shawn Hillyer, Jason Goldfine-Middleton
CS325-400: 	Project 4 

========================================================================
readme.txt
========================================================================

----------------------------------------
Usage
----------------------------------------
We have included the original city text files in the root directory for
ease of testing. These commands will output a corresponding .txt.tour
file in the root directory.

To generate our best (time-unbounded) solutions, execute the following
command(s) in the root directory. 
(WARNING: this may take a number of years to complete for a full run, 
and may find better solutions as a result):

* python3 primsSubmissionTests1to6.py test-input-1.txt
* python3 primsSubmissionTests1to6.py test-input-2.txt
* python3 primsSubmissionTests1to6.py test-input-3.txt
* python3 primsSubmissionTests1to6.py test-input-4.txt
* python3 primsSubmissionTests1to6.py test-input-5.txt
* python3 primsSubmissionTests1to6.py test-input-6.txt
* python3 primsSubmissionTest7.py test-input-7.txt
* python3 primsSubmissionTests1to6.py tsp_example_1.txt
* python3 primsSubmissionTests1to6.py tsp_example_2.txt
* python3 primsSubmissionTests1to6.py tsp_example_3.txt

TO generate our competition solutions, execute the following commands
in the root directory:

* python watch.py python3 primsSubmissionTests1to6.py test-input-1.txt
* python watch.py python3 primsSubmissionTests1to6.py test-input-2.txt
* python watch.py python3 primsSubmissionTests1to6.py test-input-3.txt
* python watch.py python3 primsSubmissionTests1to6.py test-input-4.txt
* python watch.py python3 primsSubmissionTests1to6.py test-input-5.txt
* python watch.py python3 primsSubmissionTests1to6.py test-input-6.txt
* python watch.py python3 primsSubmissionTest7.py test-input-7.txt


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

	primsSubmissionTest7.py
		Alg that calculates a MST, Depth First search to create a
                preorder traversal, and attempts to find some quick 
                improvments when using large numbers of city inputs 
                under strict time limits. Use for test-input-7.txt

	primsSubmissionTests1to6.py
		Alg that calculates a MST, Depth First search to create
                a preorder traversal, and finds improvements based on that
                traversal. If finishes within time limit, pivots to a
                different starting city to construct MST and pivots to
                a different starting city for optimizing the preorder
                traversal, eventually testing all combinations of these
                two starting points. If no time limit, will run until
                keyboard interrupt is received, or until all starting
                city combinations are optimized. Use for test-input-n.txt
                for n from 1 to 6, or tsp_example_n.txt for n from 1 to 3.

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
files are in our two solutions files and in the root directory 
for easy testing. You can copy-paste the commands below to verify 
the solutions, in the solutions directory with the pre-submitted
solutions, or in the root directory after computing a .txt.tour file
as directed above.

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
