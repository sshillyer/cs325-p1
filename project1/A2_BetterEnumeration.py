#CS 325_400_F2016 Project1 - Algo2: Better Enumeration
# Jesse Thoren, Shawn Hillyer, Jason Goldfine-Middleton


def mss_better_enum(a):
    '''
    Determines the maximum sum subarray of the array a.
    :param a: array of integers consisting of at least one positive integer
    :return: sum of the MSS, left index of the MSS, right index of the MSS
    '''

    #Initialize to the first element in the input array
    max_sum = a[0]      #Stores the sum of the MSS
    max_i = 0           #Stores the lower index of the MSS
    max_j = 0           #Stores the upper index of the MSS
    n = len(a)          #Stores the length of the input array
    
    #i: Lower Bound for sum
    for i in range(n):
        #Stores the sum of the subarray from index i to j inclusive
        #Initialized to 0
        running_sum = 0

        #j: Upper Bound for sum
        for j in range(i, n):
            #Adds next element to running_sum
            running_sum += a[j]
            
            #If running_sum > max_sum, update max_sum, max_i, max_j
            if running_sum > max_sum:
                max_sum = running_sum
                max_i = i
                max_j = j

    return max_sum, max_i, max_j

# EOF
