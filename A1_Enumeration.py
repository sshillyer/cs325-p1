#CS 325_400_F2016 Project1 - Algo1: Enumeration
# Jesse Thoren, Shawn Hillyer, Jason Goldfine-Middleton

#mss_enumerative
#Input: Array of numbers
#Output: Sum of the MSS, left index of the MSS, right index of the MSS
def mss_enumerative(a):
    #Initialize to the first element in the input array
    max_sum = a[0]    # Stores the sum of the MSS
    max_i = 0                # Stores the lower bound of the MSS
    max_j = 0 #Stores the upper bound of the MSS
    array_len = len(a) #Stores the length of the input array
    
    #i: Lower Bound for sum
    for i in range(0,array_len):

        #j: Upper Bound for sum
        for j in range(i,array_len):

            #Stores the sum of the subarray from index i to j inclusive
            #Initialized to the first element to be summed
            curr_sum = a[i]
            
            #Loop through remaining elements to be summed
            for k in range(i+1,j+1):
                curr_sum += a[k]
            
            #If a new max_sum is found, update max_sum, max_i, maxj
            if curr_sum > max_sum:
                max_sum = curr_sum
                max_i = i
                max_j = j

    return max_sum, max_i, max_j

# #Input
# user_input = input("Enter an array: ")
# for char in user_input:
#     if char in " []":
#         user_input = user_input.replace(char,'')
# user_input = user_input.split(',')
# for i in range(0,len(user_input)):
#     user_input[i] = int(user_input[i])
#
# #Output/Function call
# res, start, end = mss_enumerative(user_input)
#
