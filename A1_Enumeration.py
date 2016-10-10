#CS 325_400_F2016 Project1 - Algo1: Enumeration
#Jesse Thoren

#MAXSUBARRAY
#Input: Array of numbers
#Output: Sum of the MSS, left index of the MSS, right index of the MSS
def MAXSUBARRAY(sumArray):
    #Initialize to the first element in the input array
    maxSum = sumArray[0] #Stores the sum of the MSS
    maxi = 0 #Stores the lower bound of the MSS
    maxj = 0 #Stores the upper bound of the MSS
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
            if currSum > maxSum:
                maxSum = currSum
                maxi = i
                maxj = j

    return maxSum, maxi, maxj

#Input
user_input = input("Enter an array: ")
for char in user_input:
    if char in " []":
        user_input = user_input.replace(char,'')
user_input = user_input.split(',')
for i in range(0,len(user_input)):
    user_input[i] = int(user_input[i])

#Output/Function call
res, start, end = MAXSUBARRAY(user_input)

#Display results
print("MSS: " + str(res))
print("MSS Left Index: " + str(start))
print("MSS Right Index: " + str(end))
