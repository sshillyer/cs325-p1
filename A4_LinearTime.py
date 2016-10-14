#CS 325_400_F2016 Project1 - Algo4: Linear Time
# Jesse Thoren, Shawn Hillyer, Jason Goldfine-Middleton


def mss_linear(a):
    '''
    Linear version of MSS algorithm.
    :param a: array of numbers
    :return: sum of the MSS, left index of the MSS, right index of the MSS
    '''

    max_i = 0 #Stores the lower index of the MSS
    #Get the first non-zero entry in the array to start looking for a MSS
    while a[max_i]<0:
        max_i += 1
    
    max_j = max_i #Stores the upper index of the MSS
    max_sum = a[max_i] #Stores the sum of the MSS so far
    array_len = len(a) #Stores the length of the input array
    
    curr_sum = 0 #Stores the sum of the candidate MSS
    curr_i = max_i #Stores the lower index of the current possible MSS
    
    for j in range(max_i, array_len):
        curr_sum += a[j]

        '''
        :If a new max sum is found, save the current sum as max sum
        :Save the current possible lower index of the MSS
        :Save the current j value as the possible upper index of the MSS
        '''
        if curr_sum >= max_sum:
            max_sum = curr_sum
            max_i = curr_i
            max_j = j
        
        '''
        :If curr_sum < zero, consider the subarray up to the current index
        :and the subarray after the current index separately.
        :
        :Reset the current sum to zero. Loop until we hit the end of the
        :array or find a new positive array value to look for another MSS.
        :If a new positive array value is found, reset curr_i to the index
        :it is found at, and continue on with the for loop.
        '''
        if curr_sum < 0:
            curr_sum = 0
            while j+1 < array_len:
                if a[j+1]<0:
                    j += 1
                else:
                    break
            curr_i = j+1
    
    return max_sum, max_i, max_j

# EOF
