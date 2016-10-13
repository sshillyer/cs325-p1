#CS 325_400_F2016 Project1 - Algo3: Divide and Conquer
# Jesse Thoren, Shawn Hillyer, Jason Goldfine-Middleton



def mss_divconq_helper(a):
    '''
    Helper function for mss_divconq
    :param a: Array of values
    :return: [max_prefix_value, max_prefix_end_index, max_suffix_value, max_suffix_start_index, max_sum_value, max_left_index, max_right_index, total_sum_value]
    '''
    #If length 1 just return the value or index 0 as appropriate.
    if(len(a)==1):
        return [a[0], 0, a[0], 0, a[0], 0, 0, a[0]]
    
    #Split in half
    middle = len(a)//2

    #Get result of recursion from left and right halves
    left = mss_divconq_helper(a[:middle])
    right = mss_divconq_helper(a[middle:])

    '''
    The max prefix value is either the same as the max prefix of the 
     left half, or extends over to the right half, in which case
     it holds the entirety of left subarray and the max prefix of
     the right subarray.
    '''
    max_prefix_value = max(left[0], left[7]+right[0])

    '''
    The max suffix value is either the same as the max suffix of the
     right half, or extends over to the left half, in which case
     it holds the entirety of the right subarray and the max suffix
     of the left subarray
    '''
    max_suffix_value = max(right[2], right[7]+left[2])

    '''
    The MSS value is here. It's either the max sum that's
     entirely in the left subarray, the max sum that's entirely in the
     right subarray, or the sum of the suffix of the left and the prefix
     of the right.
    '''
    max_sum_value = max(left[4], right[4], left[2]+right[0])

    '''
    This stores the total sum of all elements in the array. It's useful
     for calculating referencing when calculating the max prefix and
     suffix values above.
    '''
    total_sum_value = left[7] + right[7]

    '''
    This sets the Max Prefix end index. It's initialized to the same
     value as the max prefix of the left subarray, but is changed in the
     case that the max prefix extends into the right subarray; in this
     case, the index falls at the end of the prefix of the right subarray
     except we adjust by adding middle to account for all elements of the
     left subarray.
    '''
    max_prefix_end_index = left[1]
    if(max_prefix_value == left[7]+right[0]):
        max_prefix_end_index = middle + right[1]

    '''
    This sets the Max Suffix start index. It's initialize to the the max
     suffix start index of the right subarray, plus the elements that are
     added when joining the left subarray. This is overridden by the 
     max suffix start index of the left subarray if the max suffix extends
     into the left subarray.
    '''
    max_suffix_start_index = middle + right[3]
    if(max_suffix_value == right[7]+left[2]):
        max_suffix_start_index = left[3]

    '''
    This sets the left and right indices that bound (inclusively) 
     the MSS. 
     In case that it's entirely contained in the left
     subarray, we take both bounds from the left subarray. 
     In case it's entirely in the right subarray, this becomes 
     the bounds of the maximum sum in the right subarray, 
     adjusted for the elements added when joining with the left subarray. 
     In case that the MSS is formed by joining a suffix of the left 
     subarray and a prefix of the right subarray, this is formed by setting
     max_left_index as max_suffix_start_index in the left subarray and
     max_right_index as max_prefix_end_index in the right subarray... adjusted
     for the elements added in joining the left and right subarrays.
    '''
    max_left_index = left[5]
    max_right_index = left[6]
    if(max_sum_value == right[4]):
        max_left_index = middle + right[5]
        max_right_index = middle + right[6]
    if(max_sum_value == left[2]+right[0]):
        max_left_index = left[3]
        max_right_index = middle+right[1]

    '''
    This returns all of the important values to the recursive call,
     or, ultimately, back to mss_enumerative
    '''
    return [max_prefix_value, max_prefix_end_index, max_suffix_value, max_suffix_start_index, max_sum_value, max_left_index, max_right_index, total_sum_value]



def mss_divconq(a):
    '''
    Divide and conquer version of MSS function
    :param a: Array of numbers
    :return: Sum of the MSS, left index of the MSS, right index of the MSS
    '''
    helper_res = mss_divconq_helper(a)
    return helper_res[4], helper_res[5], helper_res[6]

# EOF
