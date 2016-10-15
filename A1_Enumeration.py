#CS 325_400_F2016 Project1 - Algo1: Enumeration
# Jesse Thoren, Shawn Hillyer, Jason Goldfine-Middleton


def mss_enumerative(a):
    '''
    Determines the maximum sum subarray of the array a.
    :param a: array of integers consisting of at least one positive value
    :return: sum of the MSS, left index of the MSS, right index of the MSS
    '''

    #Initialize to the first element in the input array
    max_sum = a[0]      # Stores the sum of the MSS
    max_i = 0           # Stores the lower index of the MSS
    max_j = 0           # Stores the upper index of the MSS
    n = len(a)          # Stores the length of the input array
    
    #i: Lower Bound for sum
    for i in range(n):

        #j: Upper Bound for sum
        for j in range(i, n):

            #Stores the sum of the subarray from index i to j inclusive
            #Initialized to the first element to be summed
            curr_sum = a[i]
            
            #Loop through remaining elements to be summed
            for k in range(i + 1,j + 1):
                curr_sum += a[k]
            
            #If a new max_sum is found, update max_sum, max_i, max_j
            if curr_sum > max_sum:
                max_sum = curr_sum
                max_i = i
                max_j = j

    return max_sum, max_i, max_j


# TODO: USE THIS AS BASIS FOR PARSING FILE INPUT
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

# EOF
