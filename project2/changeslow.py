#Python3 implementation of change with divide and conquer (SLOW)
#Jesse Thoren, Shawn Hillyer, Jason Goldfine-Middleton

import time

def changeslow(D, a):
    minarr = [0 for x in range(len(D))]        #Stores coins used to make change for a with minamt coins
    minamt = a          #Worst case scenario is we use all "1" coins.

    if a == 0:          #Zero change left to make.
        return minarr, minamt

    #Loop through each denomination
    for i in range(0, len(D)):
        '''
        :If the denomination is too big, then skip it.
        :If it's small enough, then we use 1 of these coins and then
        :   test the amount that remains after subtracting that coin.
        '''
        if(D[i]<=a):
            #Get values from recursion
            currarr, curramt = changeslow(D,a-D[i])
            
            #Update currarr with 1 additional coin of the correct denom
            currarr[i] = currarr[i]+1

            #Update curramt with 1 additional coin
            curramt = curramt+1

            '''
            :If curramt shows that we have a better amount now than
            :   our previous best result, make minamt the newly found
            :   amount, and make minarr the newly found best array of coins.
            '''
            if minamt>=curramt:
                minamt = curramt
                minarr = currarr

    return minarr, minamt

# #User Input
# user_array = input("Enter array of denominations in increasing order: ")
# for char in user_array:
#     if char in " []":
#         user_array = user_array.replace(char,'')
# user_array = user_array.split(',')
# for i in range(0,len(user_array)):
#     user_array[i] = int(user_array[i])
#
# user_amount = int(input("Enter an amount to make change for: "))
#
#
# #Function Call
# start_time = time.time()
# arr, mincoins = changeslow(user_array, user_amount)
# end_time = time.time() - start_time
#
# #Output
# print(arr)
# print("You need to use", mincoins, "coins.")
# print("It took", end_time, "seconds to compute.")
