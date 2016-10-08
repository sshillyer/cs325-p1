#!/usr/bin/env python

#CS 325_400_F2016 Project1 - Algo1: Enumeration
#Jesse Thoren

#MAXSUBARRAY
#Input: Array of numbers
#Output: The maximum sum subarray
def MAXSUBARRAY(sumArray):
    #Initialize to the first element in the sumArray
    maxSum = sumArray[0] #Stores the sum of the maximum sum subarray
    maxi = 0 #Stores the lower bound of the maximum sum subarray
    maxj = 0 #Stores the upper bound of the maximum sum subarray
    arrayLen = len(sumArray) #Stores the length of the input array
    
    #i: Lower Bound for sum
    for i in range(0,arrayLen):

        #j: Upper Bound for sum
        for j in range(i,arrayLen):

            #Stores the sum of the subarray from index i to j inclusive
            #Initialized to the first element to be summed
            currSum = sumArray[i]
            
            #Loop through remaining elements to be summed
            for k in range(i+1,j+1):
                currSum += sumArray[k]
            
            #If a new maxSum is found, update maxSum, maxi, maxj
            if(currSum > maxSum):
                maxSum = currSum
                maxi = i
                maxj = j

    maxSubarray = sumArray[maxi:maxj+1]
    return [maxSubarray, maxSum]

#Input
user_input = input("Enter an array: ")

#Output/Function call
output = MAXSUBARRAY(user_input);

#Display results
print "Max Subarray: ", output[0]
print "Max Subarray Sum: ", output[1]
