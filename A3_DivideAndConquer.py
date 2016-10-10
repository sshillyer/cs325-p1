#!/usr/bin/env python

#CS 325_400_F2016 Project1 - Algo3: Divide and Conquer
#Jesse Thoren

#MAXSUBHELPER
#Input: Array of numbers
#Output: [MaxPrefixValue, MaxPrefixEndIndex, MaxSuffixValue, MaxSuffixStartIndex, MaxSumValue, MaxLeftValue, MaxRightValue, TotalSumValue]
def MAXSUBHELPER(a):
    #If length 1 just return the value or index 0 as appropriate.
    if(len(a)==1):
        return [a[0], 0, a[0], 0, a[0], 0, 0, a[0]]
    
    #Split in half
    middle = len(a)//2

    #Get result of recursion from left and right halves
    left = MAXSUBHELPER(a[:middle])
    right = MAXSUBHELPER(a[middle:])

    '''
    The max prefix value is either the same as the max prefix of the 
     left half, or extends over to the right half, in which case
     it holds the entirety of left subarray and the max prefix of
     the right subarray.
    '''
    MaxPrefixValue = max(left[0], left[7]+right[0])

    '''
    The max suffix value is either the same as the max suffix of the
     right half, or extends over to the left half, in which case
     it holds the entirety of the right subarray and the max suffix
     of the left subarray
    '''
    MaxSuffixValue = max(right[2], right[7]+left[2])

    '''
    The max sum of a subarray is here. It's either the max sum that's
     entirely in the left subarray, the max sum that's entirely in the
     right subarray, or the sum of the suffix of the left and the prefix
     of the right.
    '''
    MaxSumValue = max(left[4], right[4], left[2]+right[0])

    '''
    This stores the total sum of all elements in the array. It's useful
     for calculating referencing when calculating the max prefix and
     suffix values above.
    '''
    TotalSumValue = left[7] + right[7]

    '''
    This sets the Max Prefix end index. It's initialized to the same
     value as the max prefix of the left subarray, but is changed in the
     case that the max prefix extends into the right subarray; in this
     case, the index falls at the end of the prefix of the right subarray
     except we adjust by adding middle to account for all elements of the
     left subarray.
    '''
    MaxPrefixEndIndex = left[1]
    if(MaxPrefixValue == left[7]+right[0]):
        MaxPrefixEndIndex = middle + right[1]

    '''
    This sets the Max Suffix start index. It's initialize to the the max
     suffix start index of the right subarray, plus the elements that are
     added when joining the left subarray. This is overridden by the 
     max suffix start index of the left subarray if the max suffix extends
     into the left subarray.
    '''
    MaxSuffixStartIndex = middle + right[3]
    if(MaxSuffixValue == right[7]+left[2]):
        MaxSuffixStartIndex = left[3]

    '''
    This sets the left and right indices that bound (inclusively) 
     the maximum sum subarray. In case that it's entirely contained in
     the left subarray, we take both bounds from the left subarray. In case
     it's entirely in the right subarray, this becomes the bounds of the
     maximum sum in the right subarray, adjusted for the elements added
     when joining with the left subarray. In case that the maximum sum
     subarray is formed by joining a suffix of the left subarray and
     a prefix of the right subarray, this is formed by setting
     MaxLeftIndex as MaxSuffixStartIndex in the left subarray and
     MaxRightIndex as MaxPrefixEndIndex in the right subarray... adjusted
     for the elements added in joining the left and right subarrays.
    '''
    MaxLeftIndex = left[5] 
    MaxRightIndex = left[6]
    if(MaxSumValue == right[4]):
        MaxLeftIndex = middle + right[5]
        MaxRightIndex = middle + right[6]
    if(MaxSumValue == left[2]+right[0]):
        MaxLeftIndex = left[3]
        MaxRightIndex = middle+right[1]

    '''
    This returns all of the important values to the recursive call,
     or, ultimately, back to MAXSUBARRAY
    '''
    return [MaxPrefixValue, MaxPrefixEndIndex, MaxSuffixValue, MaxSuffixStartIndex, MaxSumValue, MaxLeftIndex, MaxRightIndex, TotalSumValue]


#MAXSUBARRAY
#Input: Array of numbers
#Output: [The maximum sum subarray, The sum of the maximum sum subarray]
def MAXSUBARRAY(sumArray):
    helperRes = MAXSUBHELPER(sumArray)
    '''
    This returns the original array spliced to the bounds of the maximum
     sum subarray returned by the helper function, and the actual
     maximum sum of the maximum sum subarray
    '''
    return [sumArray[helperRes[5]:helperRes[6]+1], helperRes[4]]

#Input
user_input = input("Enter an array: ")

#Output/Function call
output = MAXSUBARRAY(user_input)

#Display results
print "Max Subarray: ", output[0]
print "Max Subarray Sum: ", output[1]
