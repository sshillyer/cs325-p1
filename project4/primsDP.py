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
        v.children = []
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
        minV.parent.children.append(minV)
        MST.append(Edge(minV,minV.parent))
        #Check to see if the path through V is closer - updates the pQueue
        for v in cities:
            if v.priority > graph.get_distance_between_vertices(minV, v):
                v.priority = graph.get_distance_between_vertices(minV, v)
                v.parent = minV
    return MST

#Run after primsMST
def dfsTraversal(cities):
    for v in cities:
        v.visited = False
    preorderTraversal = []
    DFS(cities[0], preorderTraversal)
    #Nodes stored in order, then return to first index.
    return preorderTraversal

#Run in dfsTraversal
def DFS(currentNode, preorderTraversal):
    preorderTraversal.append(currentNode)
    currentNode.visited = True
    for v in currentNode.children:
        DFS(v, preorderTraversal)

#Run with a list of cities in the order you want to travel them
def calculateTraversalDistance(traversalOrder, graph):
    totalDistance = 0
    for i in range(len(traversalOrder)-1):
        totalDistance += graph.get_distance_between_vertices(traversalOrder[i], traversalOrder[(i+1)%len(traversalOrder)])
    return totalDistance


cities = read_city_data_from_file("./provided/tsp_example_3.txt")
graph = TspGraphMatrix(cities)
MST = primsMST(cities,graph)
traversalOrder = dfsTraversal(cities)
print("Distance of preorder traversal: " + str(calculateTraversalDistance(traversalOrder, graph)))
