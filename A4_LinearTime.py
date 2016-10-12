#CS 325_400_F2016 Project1 - Algo4: Linear Time
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
res, start, end = MAXSUBARRAY(user_input);

#Display results
print("MSS: " + str(res))
print("MSS Left Index: " + str(start))
print("MSS Right Index: " + str(end))
