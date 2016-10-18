#Python3 implementation of change with dynamic programming
#Jesse Thoren, Shawn Hillyer, Jason Goldfine-Middleton

import time, resource, sys

#Researched recursion limit stackoverflow.com/questions/5061582
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

change_memo={}
def changedp(D, a):
    minarr = []         #Stores coins used to make change for a with minamt coins
    for i in range(0,len(D)):
        minarr.append(0)
    minamt = a          #Worst case scenario is we use all "1" coins

    if a == 0:          #Zero change left to make.
        return minarr, minamt

    if a not in change_memo:
        for i in range(0, len(D)):
            if(D[i]<=a):
                passedarr, curramt = changedp(D,a-D[i])
                currarr = []
                for j in range(0, len(passedarr)):
                    currarr.append(passedarr[j])
                currarr[i] = currarr[i]+1
                curramt = curramt+1
                if minamt>curramt:
                    minamt = curramt
                    minarr = currarr
                change_memo[a] = [minarr, minamt]
    return change_memo[a]

user_array = input("Enter array of denominations in increasing order: ")
for char in user_array:
    if char in " []":
        user_array = user_array.replace(char,'')
user_array = user_array.split(',')
for i in range(0,len(user_array)):
    user_array[i] = int(user_array[i])

user_amount = int(input("Enter an amount to make change for: "))


start_time = time.time()
arr, mincoins = changedp(user_array, user_amount)
end_time = time.time() - start_time

print(arr)
print("You need to use", mincoins, "coins.")
print("It took", end_time, "to compute.")
