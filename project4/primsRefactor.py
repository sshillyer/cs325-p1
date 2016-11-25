#Prims MST algorithm pseudocode researched at: people.cs.pitt.edu/~mnugent/notes/fall2012/prim,%20tsp%20approx.pdf

from tsp_helper_functions import *
import signal
import sys

def signal_handler(signal, frame):
    print("Signal Received, dumping best result so far to", outputFilename)
    dumpToFile(minimum, bestTraversal, outputFilename)
    #dumpOut(minimum, bestTraversal)
    sys.exit(0)

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
    
    #Create a list to store the MST Edges
    MST = []

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

#Run after primsMST
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

#Run in dfsTraversal
def DFS(currentNode, preorderTraversal):
    preorderTraversal.append(currentNode)
    currentNode.visited = True
    for v in currentNode.child:
        DFS(v, preorderTraversal)

#Run with a list of edges to calculate the distance of all edges
def calculateTraversalDistance(traversalOrder):
    totalDistance = 0
    for v in traversalOrder:
        totalDistance += graph.get_distance_between_vertices(v,v.child)
    return totalDistance

#
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

def iterateTwoOpt(cities,graph,times,initialTraversal):
    currentBest = initialTraversal
    for i in range(times):
        previousBest = currentBest
        previousTime = calculateTraversalDistance(previousBest)
        currentBest = twoOpt(cities,graph,previousBest)
        print("Current best distance after " + str(i+1) + " iterations: " +str(calculateTraversalDistance(currentBest)))
        if previousTime == calculateTraversalDistance(currentBest):
            break        
    return currentBest
        

#Only run if cities parent/child relationship forms a walk.
#This happens first during dfsTraversal
def buildTraversal(cities,graph):
    traversalList = []
    traversalList.append(cities[0])
    currNode = cities[0].child
    while currNode!=cities[0]:
        traversalList.append(currNode)
        currNode = currNode.child
    return traversalList

def rotateCities(cities, n):
    r = n%len(cities)
    return cities[r:] + cities[:r]

def dumpOut(minimum, bestTraversal):
    print(str(minimum))
    for i in bestTraversal:
        print(i.label)

def dumpToFile(minimum, bestTraversal, filename):
    text_file = open(filename, "w")
    print(str(minimum), file = text_file)
    for i in bestTraversal:
        print(i.label, file = text_file)
    text_file.close()

sys.setrecursionlimit(10**6)
#print(sys.getrecursionlimit())
inputFilename = ""
if len(sys.argv)==1:
    print("Usage: python3 primsRefactor.py inputFilename")
    sys.exit(0)
else:
    inputFilename = sys.argv[1]
outputFilename = inputFilename + ".tour"

cities = read_city_data_from_file(inputFilename)
graph = TspGraphMatrix(cities)
primsMST(cities,graph)
traversalOrder = dfsTraversal(cities,graph)
minimum = calculateTraversalDistance(traversalOrder)
bestTraversal = traversalOrder
#print("Distance of preorder traversal: " + str(minimum))
#Ok to catch signals to dump if we make it this far.

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

for i in range(len(cities)):
    primsMST(cities,graph)
    dfsTraversal(cities,graph)
    #1000003 is prime, so len(cities)%1000003 is relatively prime to
    #len(cities) for len(cities)<1000003
    #This assures that all the starting points get tested
    cities = rotateCities(cities,1000003)
    optimized = iterateTwoOpt(cities,graph, 50, traversalOrder)
    optimizedDistance = calculateTraversalDistance(optimized)
    if optimizedDistance < minimum:
        minimum = optimizedDistance
        bestTraversal = optimized
    print("Final optimized distance rotation", str(i+1), ": ", str(optimizedDistance))
    print("Best so far: ", str(minimum))

dumpToFile(minimum, bestTraversal, outputFilename)
#print("Final Results: ")
#dumpOut(minimum, bestTraversal)
