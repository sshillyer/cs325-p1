#Prims MST algorithm pseudocode researched at: people.cs.pitt.edu/~mnugent/notes/fall2012/prim,%20tsp%20approx.pdf

from tsp_helper_functions import *
from Edge import *

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
        MST.append(Edge(minV,minV.parent,graph.get_distance_between_vertices(minV,minV.parent)))
        #Check to see if the path through V is closer - updates the pQueue
        for v in cities:
            if v.priority > graph.get_distance_between_vertices(minV, v):
                v.priority = graph.get_distance_between_vertices(minV, v)
                v.parent = minV
    return MST

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

    #Convert preorderTraversal to an edge list
    preorderTraversal = buildEdgeList(cities,graph)
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
    for e in traversalOrder:
        #print(e.u.label + " " + e.v.label)
        totalDistance += e.distance
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
            newBest = buildEdgeList(cities,graph)
            currentBest = newBest

    return currentBest

def iterateTwoOpt(cities,graph,times,initialTraversal):
    currentBest = initialTraversal
    for i in range(times):
        previousBest = currentBest
        currentBest = twoOpt(cities,graph,previousBest)
        print("Current best distance after " + str(i+1) + " iterations: " +str(calculateTraversalDistance(currentBest)))
        if calculateTraversalDistance(previousBest) == calculateTraversalDistance(currentBest):
            break        
    return currentBest
        

#Only run if cities parent/child relationship forms a walk.
#This happens first during dfsTraversal
def buildEdgeList(cities,graph):
    edgeList = []
    edgeList.append(Edge(cities[0],cities[0].child, graph.get_distance_between_vertices(cities[0],cities[0].child)))
    currNode = cities[0].child
    while currNode!=cities[0]:
        edgeList.append(Edge(currNode,currNode.child,graph.get_distance_between_vertices(currNode,currNode.child)))
        currNode = currNode.child
    return edgeList


cities = read_city_data_from_file("./provided/tsp_example_3.txt")
graph = TspGraphMatrix(cities)
MST = primsMST(cities,graph)
traversalOrder = dfsTraversal(cities,graph)
optimized = iterateTwoOpt(cities,graph, 50, traversalOrder)
print("Distance of preorder traversal: " + str(calculateTraversalDistance(traversalOrder)))
print("Final optimized distance: ", str(calculateTraversalDistance(optimized)))
#print("Two opt iterated through all combinations once: " + str(calculateTraversalDistance(optimize1)))
#print("Two opt iterated through all combinations twice: " + str(calculateTraversalDistance(optimize2)))
#print("Two opt iterated through all combinations thrice: " + str(calculateTraversalDistance(optimize3)))
