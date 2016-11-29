#Prims MST algorithm pseudocode researched at: people.cs.pitt.edu/~mnugent/notes/fall2012/prim,%20tsp%20approx.pdf

from tsp_helper_functions import *
import signal
import sys

#Handles terminate signals and interrupt signals by dumping the
#best file so far to a .txt.tour file
def signal_handler(signal, frame):
    print("Signal Received, dumping best result so far to", outputFilename)
    dumpToFile(minimum, bestTraversal, outputFilename)
    #dumpOut(minimum, bestTraversal)
    sys.exit(0)

#Input: array of city objects, graph storing distances between any 2 cities
#Postconditions: The cities in city array have a parent/child relationship
#                that forms a Minimum Spanning Tree of all cities
def primsMST(cities, graph):
    #Choose start vertex u from cities
    root = cities[0]
    #print("Amount of cities: " + str( len(cities)))
    
    #Set priority to the distance to root, Set parent to root for all cities
    for v in cities:
        v.priority = graph.get_distance_between_vertices(root,v)
        v.parent = root
        v.child = []
    root.priority = -1
    
    #Assign len(cities)-1 edges to the MST
    for i in range(0, len(cities)-1):
        minP = float("inf")
        minV = None
        #Get the lowest priority city
        for v in cities:
            #print(v.priority)
            if v.priority >= 0 and v.priority < minP:
                minP = v.priority
                minV = v
        #print("Connection " + str(i+1) + ": " + str(minV.priority))
        minV.priority = -1
        minV.parent.child.append(minV)
        #Check to see if the path through V is closer - updates the pQueue
        for v in cities:
            if v.priority > graph.get_distance_between_vertices(minV, v):
                v.priority = graph.get_distance_between_vertices(minV, v)
                v.parent = minV

#Preconditions: Run after primsMST
#Input: Array of Cities, Graph storing distances between any 2 cities
#Output: Returns a preorder traversal of the parent/child relationship
#        formed by primsMST
#Postconditions: The parent child relationship from primsMST is replaced
#                by a parent/child relationship corresponding to a tour
def dfsTraversal(cities, graph):
    for v in cities:
        v.visited = False
    preorderTraversal = []
    DFS(cities[0], preorderTraversal)
    #preorderTraversal now holds a valid preorder traversal.
    
    #Convert the MST parent/child relationship into a walk.
    for i in range(len(preorderTraversal)):
        #Assign parent to prior element in preorder Traversal
        preorderTraversal[i].parent = preorderTraversal[(i-1+len(preorderTraversal))%len(preorderTraversal)]
        #Assign child to next element in preorder Traversal
        preorderTraversal[i].child = preorderTraversal[(i+1)%len(preorderTraversal)]

    return preorderTraversal

#DFS is a helper for the depth first search required by dfsTraversal
def DFS(currentNode, preorderTraversal):
    preorderTraversal.append(currentNode)
    currentNode.visited = True
    for v in currentNode.child:
        DFS(v, preorderTraversal)

#Takes in a list of cities and calculates the distance between each
#city in the list and its child.
#This need not take in a traversal, but if it takes in a valid tour
#this will compute the length of the entire tour.
def calculateTraversalDistance(traversalOrder):
    totalDistance = 0
    for v in traversalOrder:
        totalDistance += graph.get_distance_between_vertices(v,v.child)
    return totalDistance

#Preconditions: Run only if the parent/child relationship in the cities
#               array forms a valid walk. This happens after dfsTraversal
#               for the first time.
#Input: Array of cities, graph storing distances between any 2 cities,
#       any valid traversal to optimize.
#Output: The best optimized traversal after one pass of all combinations
#        of cities in the cities array.
#        This method tests every pair once.
#        This method is designed to be iterated until no improvements are
#        found.
#Postconditions: Cities parent/child relationship is changed, but
#                remains a valid walk.
def twoOpt(cities,graph,traversalToOptimize):
    currentBest = traversalToOptimize
    for i in cities:
        for j in cities:
            #check if they're the same point or adjacent points to skip.
            if i == j:
                continue
            if i.child == j:
                continue
            if i == j.child:
                continue

            #skip if not better
            original = graph.get_distance_between_vertices(i, i.child) + graph.get_distance_between_vertices(j, j.child)
            improvement = graph.get_distance_between_vertices(i,j) + graph.get_distance_between_vertices(i.child, j.child)
            if improvement >= original:
                continue

            #reconstruct path if better
            city1childchildtemp = i.child.child
            i.child.child = j.child
            j.child.parent = i.child

            currcity = j
            while 1:
                if currcity == i.child:
                    currcity.parent = city1childchildtemp
                    break
                temp = currcity.child
                currcity.child = currcity.parent
                currcity.parent = temp
                currcity = currcity.child

            j.parent = i
            i.child = j

            #Rebuild so we have a current preorderTraversal
            #newBest = buildTraversal(cities,graph)
            #currentBest = newBest
            #print("Update: " + str(calculateTraversalDistance(currentBest)))

    currentBest = buildTraversal(cities,graph)
    return currentBest

#Iterates 2-opt a configurable number of times.
def iterateTwoOpt(cities,graph,times,initialTraversal):
    currentBest = initialTraversal
    for i in range(times):
        previousBest = currentBest
        previousTime = calculateTraversalDistance(previousBest)
        currentBest = twoOpt(cities,graph,previousBest)
        #print("Current best distance after " + str(i+1) + " iterations: " +str(calculateTraversalDistance(currentBest)))
        if previousTime == calculateTraversalDistance(currentBest):
            break        
    return currentBest
        

#Only run if cities parent/child relationship forms a walk.
#This happens first during dfsTraversal
#The buildTraversal method uses the parent/child relationship to
#build an array of cities in traversal order, which will form a valid walk
#of all cities if run after dfsTraversal
def buildTraversal(cities,graph):
    traversalList = []
    traversalList.append(cities[0])
    currNode = cities[0].child
    while currNode!=cities[0]:
        traversalList.append(currNode)
        currNode = currNode.child
    return traversalList

#Returns a copy of the inputted list of cities (or traversal walk)
#That has been rotated to a different initial point.
#This is useful for beginning optimizations at a different starting city.
def rotateCities(cities, n):
    r = n%len(cities)
    return cities[r:] + cities[:r]

#Use this to dump the minimum value and best Traversal order to the screen
def dumpOut(minimum, bestTraversal):
    print(str(minimum))
    for i in bestTraversal:
        print(i.label)

#Use this to dump the minimum value and best Traversal order to a tour file
def dumpToFile(minimum, bestTraversal, filename):
    text_file = open(filename, "w")
    print(str(minimum), file = text_file)
    for i in bestTraversal:
        print(i.label, file = text_file)
    text_file.close()

########Main method

#Raise recursion limit for large amounts of cities. (Required for DFS)
sys.setrecursionlimit(10**6)

#Process filename naming scheme
inputFilename = ""
if len(sys.argv)==1:
    print("Usage: python3 primsRefactor.py inputFilename")
    sys.exit(0)
else:
    inputFilename = sys.argv[1]
outputFilename = inputFilename + ".tour"

#Get cities from file
cities = read_city_data_from_file(inputFilename)
#Form a graph of distances between any 2 cities
graph = TspGraphMatrix(cities)
#Get cities parent/child relationship into a minimal spanning tree
primsMST(cities,graph)
#Get a preorder traversal from the MST found in the previous line
traversalOrder = dfsTraversal(cities,graph)
#Set the length of the walk of the preorder traversal as our initial min
minimum = calculateTraversalDistance(traversalOrder)
#Stores a copy of the initial traversal info in case needed later
traversalCopy = minimum
bestTraversal = traversalOrder
#Stores the i number for the rotation of the best initial rotation for
#the traversal number
bestRot = None
bestCityRot = None
#Get to a good starting rotation
cityRot = 0
rot = 3
if(len(cities)>50):
    cityRot = 93
    rot = 56
if(len(cities)>100):
    cityRot = 226
    rot = 204
if(len(cities)>250):
    cityRot = 25
    rot = 379
if(len(cities)>500):
    cityRot = 2
    rot = 541
if(len(cities)>1000):
    cityRot = 0
    rot = 17
if(len(cities)>2000):
    cityRot = 0
    rot = 0
#print("Distance of preorder traversal: " + str(minimum))

#Ok to catch signals to dump if we make it this far.
#Set how to handle sigint and sigterm
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

#Loop through every combination of city rotations and traversal rotations
#This looks for the best local minimum we can find with our alg
#Rotate through all starting cities for building a MST
for i in range(len(cities)):
    cities = rotateCities(cities,1+cityRot)
    #Rotate through all starting traversal points for optimizing 2opt
    for j in range(len(traversalOrder)):
        primsMST(cities,graph)
        traversalOrder = dfsTraversal(cities,graph)
        traversalOrder = rotateCities(traversalOrder,j+rot)
        optimized = iterateTwoOpt(traversalOrder,graph, 50, traversalOrder)
        optimizedDistance = calculateTraversalDistance(optimized)
        if optimizedDistance < minimum:
            minimum = optimizedDistance
            bestTraversal = optimized
            bestRot = j
            bestCityRot = i
        #print("Final optimized distance rotation", str(i+1),".", str(j), ": ", str(optimizedDistance))
        #print("Best so far:", str(minimum))
        #print("Best CityRot:", str(bestCityRot))
        #print("Best TraversalRot:", str(bestRot))
#print("Original Traversal:", traversalCopy)
#print("Best Rotations- City Rotation:",bestCityRot + 1, " Traversal Rotation:", bestRot)

#Dumps the best result to the file if we make it to the end before time has elapsed (for competition cases), or a keyboard interrupt.
print("Optimization complete. Outputting to:", outputFilename)
dumpToFile(minimum, bestTraversal, outputFilename)
print("Output complete.")
#print("Final Results: ")
#dumpOut(minimum, bestTraversal)
