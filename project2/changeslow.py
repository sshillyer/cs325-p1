#Python3 implementation of change with divide and conquer (SLOW)
#Jesse Thoren, Shawn Hillyer, Jason Goldfine-Middleton

import time

def changeslow(D, a):
    minarr = []         #Stores coins used to make change for a with minamt coins
    for i in range(0,len(D)):
        minarr.append(0)
    minamt = a          #Worst case scenario is we use all "1" coins.

    if a == 0:          #Zero change left to make.
        return minarr, minamt

    for i in range(0, len(D)):
        if(D[i]<=a):
            currarr, curramt = changeslow(D,a-D[i])
            currarr[i] = currarr[i]+1
            curramt = curramt+1
            if minamt>curramt:
                minamt = curramt
                minarr = currarr
    return minarr, minamt

user_array = input("Enter array of denominations in increasing order: ")
for char in user_array:
    if char in " []":
        user_array = user_array.replace(char,'')
user_array = user_array.split(',')
for i in range(0,len(user_array)):
    user_array[i] = int(user_array[i])

user_amount = int(input("Enter an amount to make change for: "))


start_time = time.time()
arr, mincoins = changeslow(user_array, user_amount)
end_time = time.time() - start_time

print(arr)
print("You need to use", mincoins, "coins.")
print("It took", end_time, "seconds to compute.")
