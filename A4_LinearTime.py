#!/usr/bin/env python

#CS 325_400_F2016 Project1 - Algo4: Linear Time
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
    
    #j: Find proper upper bound
    currSum = 0
    for j in range(0,arrayLen):
        currSum += sumArray[j]
        if(currSum>maxSum):
            maxSum = currSum
            maxj = j

    #i: Find proper lower bound
    currSum = maxSum
    for i in range(0, maxj+1):
        #These are reversed from the first loop because subtracting
        #   out a term would move maxi to the next index
        if(currSum>maxSum):
            maxSum = currSum
            maxi = i
        currSum -= sumArray[i]


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
