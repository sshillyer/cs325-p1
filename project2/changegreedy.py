#Python3 implementation of change with a greedy alg
#Jesse Thoren, Shawn Hillyer, Jason Goldfine-Middleton

import time

def changegreedy(D, a):
    minarr = []         #Stores coins used to make change for a with minamt coins.
    for i in range(0,len(D)):
        minarr.append(0)
    minamt = 0          #Stores min amount of coins

    #Loop through denomination array backwards to test big coins first.
    for i in range(len(D)-1, -1, -1):
        while(a>=D[i]):
            minarr[i] = minarr[i]+1
            a = a - D[i]
            minamt = minamt +1
    return minarr, minamt
#
# #User input
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
# #Function call
# start_time = time.time()
# arr, mincoins = changegreedy(user_array, user_amount)
# end_time = time.time() - start_time
#
# #Results
# print(arr)
# print("You need to use", mincoins, "coins.")
# print("It took", end_time, "seconds to compute.")
