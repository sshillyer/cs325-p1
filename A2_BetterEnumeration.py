#CS 325_400_F2016 Project1 - Algo2: Better Enumeration
# Jesse Thoren, Shawn Hillyer, Jason Goldfine-Middleton


def mss_better_enum(a):
    '''
    Determines the maximum sum subarray of the array a
    :param a:  Array of integers consisting of at least one positive integer
    :return: Sum of the MSS, left index of the MSS, right index of the MSS
    '''

    #Initialize to the first element in the input array
    max_sum = a[0] #Stores the sum of the MSS
    max_i = 0 #Stores the lower bound of the MSS
    max_j = 0 #Stores the upper bound of the MSS
    n = len(a) #Stores the length of the input array
    
    #i: Lower Bound for sum
    for i in range(0,n):
        #Stores the sum of the subarray from index i to j inclusive
        #Initialized to 0
        running_sum = 0

        #j: Upper Bound for sum
        for j in range(i,n):
            #Adds next element to running_sum
            running_sum += a[j]
            
            #If running_sum > max_sum, update max_sum, max_i, max_j
            if(running_sum > max_sum):
                max_sum = running_sum
                max_i = i
                max_j = j

    return max_sum, max_i, max_j




#Input
# user_input = input("Enter an array: ")
# for char in user_input:
#     if char in " []":
#         user_input = user_input.replace(char,'')
# user_input = user_input.split(',')
# for i in range(0,len(user_input)):
#     user_input[i] = int(user_input[i])
# print(user_input);

#Output/Function call
# res, start, end = mss_better_enum(user_input);

#Display results
# print("MSS: " + str(res))
# print("MSS Left Index: " + str(start))
# print("MSS Right Index: " + str(end))
