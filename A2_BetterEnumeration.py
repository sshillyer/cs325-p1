#CS 325_400_F2016 Project1 - Algo2: Better Enumeration
# Jesse Thoren, Shawn Hillyer, Jason Goldfine-Middleton

#mss_enumerative
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

    return maxSum, maxi, maxj

#Input
user_input = input("Enter an array: ")
for char in user_input:
    if char in " []":
        user_input = user_input.replace(char,'')
user_input = user_input.split(',')
for i in range(0,len(user_input)):
    user_input[i] = int(user_input[i])
print(user_input);

#Output/Function call
res, start, end = MAXSUBARRAY(user_input);

#Display results
print("MSS: " + str(res))
print("MSS Left Index: " + str(start))
print("MSS Right Index: " + str(end))
