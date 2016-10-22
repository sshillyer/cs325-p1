#Python3 implementation of change with dynamic programming
#Jesse Thoren, Shawn Hillyer, Jason Goldfine-Middleton

import time, sys#, resources

# Researched recursion limit stackoverflow.com/questions/5061582
# resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

def changedp(D, a):
    global change_memo
    change_memo = {}
    return changedphelper(D,a)


def changedphelper(D, a):
    minarr = [0 for x in range(len(D))]         #Stores coins used to make change for a with minamt coins
    minamt = a          #Worst case scenario is we use all "1" coins

    if a == 0:          #Zero change left to make.
        return minarr, minamt

    #If the current amount hasn't been processed, process and add to memo
    if a not in change_memo:
        #Loop through each denomination
        for i in range(len(D)):
            '''
            :If the denomination is too big, then skip it.
            :If it's small enough, then we use 1 of these coins and then
            :   test the amount that remains after subtracting that coin.
            '''
            if D[i] <= a:
                #Get values from recursion
                currarr, curramt = changedphelper(D, a - D[i])
                
                '''
                :If curramt shows that we have a better amount now than
                :   our previous best result, make minamt the newly found
                :   amount, and make minarr the newly found best array of
                :   coins.
                '''
                if minamt >= curramt + 1:
                    minamt = curramt + 1
                    minarr = currarr[:]
                    minarr[i] += 1
            
            #Save the best results to the memo.
            change_memo[a] = [minarr, minamt]

    return change_memo[a]

#User input
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
# #Function call
# start_time = time.time()
# arr, mincoins = changedp(user_array, user_amount)
# end_time = time.time() - start_time
#
# #Output
# print(arr)
# print("You need to use", mincoins, "coins.")
# print("It took", end_time, "seconds to compute.")
