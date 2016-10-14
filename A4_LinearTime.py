#CS 325_400_F2016 Project1 - Algo4: Linear Time
# Jesse Thoren, Shawn Hillyer, Jason Goldfine-Middleton


def mss_linear(a):
    '''
    Linear version of MSS algorithm.
    :param a: array of numbers
    :return: sum of the MSS, left index of the MSS, right index of the MSS
    '''

    #Initialize to the first element in the input array
    max_sum = a[0] #Stores the sum of the MSS
    max_i = 0 #Stores the lower bound of the MSS
    max_j = 0 #Stores the upper bound of the MSS
    array_len = len(a) #Stores the length of the input array
    
    #j: Find proper upper bound
    curr_sum = 0
    for j in range(array_len):
        curr_sum += a[j]
        if curr_sum >= max_sum:
            max_sum = curr_sum
            max_j = j

    #i: Find proper lower bound
    curr_sum = max_sum
    for i in range(max_j + 1):
        #These are reversed from the first loop because subtracting
        #   out a term would move max_i to the next index
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_i = i
        curr_sum -= a[i]

    return max_sum, max_i, max_j

# EOF
