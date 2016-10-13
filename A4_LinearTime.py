#CS 325_400_F2016 Project1 - Algo4: Linear Time
# Jesse Thoren, Shawn Hillyer, Jason Goldfine-Middleton

#mss_enumerative
#Input: Array of numbers
#Output: Sum of the MSS, left index of the MSS, right index of the MSS
def mss_linear(a):
    #Initialize to the first element in the input array
    max_sum = a[0] #Stores the sum of the MSS
    max_i = 0 #Stores the lower bound of the MSS
    max_j = 0 #Stores the upper bound of the MSS
    arrayLen = len(a) #Stores the length of the input array
    
    #j: Find proper upper bound
    curr_sum = 0
    for j in range(0,arrayLen):
        curr_sum += a[j]
        if(curr_sum>max_sum):
            max_sum = curr_sum
            max_j = j

    #i: Find proper lower bound
    curr_sum = max_sum
    for i in range(0, max_j+1):
        #These are reversed from the first loop because subtracting
        #   out a term would move max_i to the next index
        if(curr_sum>max_sum):
            max_sum = curr_sum
            max_i = i
        curr_sum -= a[i]

    return max_sum, max_i, max_j

# #Input
# user_input = input("Enter an array: ")
# for char in user_input:
#     if char in " []":
#         user_input = user_input.replace(char,'')
# user_input = user_input.split(',')
# for i in range(0,len(user_input)):
#     user_input[i] = int(user_input[i])
#
# #Output/Function call
# res, start, end = mss_linear(user_input);
#
# #Display results
# print("MSS: " + str(res))
# print("MSS Left Index: " + str(start))
# print("MSS Right Index: " + str(end))
