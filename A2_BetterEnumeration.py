#!/usr/bin/env python

#CS 325_400_F2016 Project1 - Algo2: Better Enumeration
#Jesse Thoren

#MAXSUBARRAY
#Input: Array of numbers
#Output: [The maximum sum subarray, The sum of the maximum sum subarray]
def MAXSUBARRAY(sumArray):
    #Initialize to the first element in the sumArray
    maxSum = sumArray[0] #Stores the sum of the maximum sum subarray
    maxi = 0 #Stores the lower bound of the maximum sum subarray
    maxj = 0 #Stores the upper bound of the maximum sum subarray
    arrayLen = len(sumArray) #Stores the length of the input array
    
    #i: Lower Bound for sum
    for i in range(0,arrayLen):
        #Stores the sum of the subarray from index i to j inclusive
        #Initialized to 0
        runningSum = 0

        #j: Upper Bound for sum
        for j in range(i,arrayLen):
            #Adds next element to runningSum
            runningSum += sumArray[j]
            
            #If runningSum > maxSum, update maxSum, maxi, maxj
            if(runningSum > maxSum):
                maxSum = runningSum
                maxi = i
                maxj = j

    #Splice the input array to get the max Subarray
    maxSubarray = sumArray[maxi:maxj+1]
    return [maxSubarray, maxSum]

#Input
user_input = input("Enter an array: ")

#Output/Function call
output = MAXSUBARRAY(user_input);

#Display results
print "Max Subarray: ", output[0]
print "Max Subarray Sum: ", output[1]
