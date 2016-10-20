#Python3 implementation of change with dynamic programming
#Jesse Thoren, Shawn Hillyer, Jason Goldfine-Middleton

import time, resource, sys

#Researched recursion limit stackoverflow.com/questions/5061582
#resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

change_memo={}
def changedp(D, a):
    minarr = []         #Stores coins used to make change for a with minamt coins
    for i in range(0,len(D)):
        minarr.append(0)
    minamt = a          #Worst case scenario is we use all "1" coins

    if a == 0:          #Zero change left to make.
        return minarr, minamt

    #Conservative estimate for when we can stop being greedy
    toobig = D[len(D)-1]*(D[len(D)-1])
    extracoins = 0

    '''
    :Trim a down to just before the toobig estimate, and save the amount
    :of large coins we used to get there.
    '''
    if(a>=toobig+D[len(D)-1]):
        temp = a-toobig
        extracoins = temp//D[len(D)-1]
        temp = temp%D[len(D)-1]
        a = temp + toobig


    #If the current amount hasn't been processed, process and add to memo
    if a not in change_memo:
        #Loop through each denomination
        for i in range(0, len(D)):
            '''
            :If the denomination is too big, then skip it.
            :If it's small enough, then we use 1 of these coins and then
            :   test the amount that remains after subtracting that coin.
            '''
            if(D[i]<=a):
                #Get values from recursion
                passedarr, curramt = changedp(D,a-D[i])
                
                '''
                :Since changedp passes change_memo[a], passedarr is
                :   passed by reference. The following makes currarr a
                :   copy of passedarr as if it was passed by value.
                '''
                currarr = []
                for j in range(0, len(passedarr)):
                    currarr.append(passedarr[j])
                
                #Update currarr with 1 additional coin of the correct denom
                currarr[i] = currarr[i]+1
                
                #Update curramt with 1 additional coin
                curramt = curramt+1
                
                '''
                :If curramt shows that we have a better amount now than
                :   our previous best result, make minamt the newly found
                :   amount, and make minarr the newly found best array of
                :   coins.
                '''
                if minamt>curramt:
                    minamt = curramt
                    minarr = currarr
            
            #Save the best results to the memo.
            change_memo[a] = [minarr, minamt]

    #Prep solution for return by adding the extra coins in the req. spots
    res = change_memo[a]
    if extracoins>0:
        res[0][len(D)-1] = res[0][len(D)-1] + extracoins
        res[1] = res[1] + extracoins

    return res

#User input
user_array = input("Enter array of denominations in increasing order: ")
for char in user_array:
    if char in " []":
        user_array = user_array.replace(char,'')
user_array = user_array.split(',')
for i in range(0,len(user_array)):
    user_array[i] = int(user_array[i])

user_amount = int(input("Enter an amount to make change for: "))


#Function call
start_time = time.time()
arr, mincoins = changedp(user_array, user_amount)
end_time = time.time() - start_time

#Output
print(arr)
print("You need to use", mincoins, "coins.")
print("It took", end_time, "seconds to compute.")
