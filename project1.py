# Algorithm 1: Enumeration.
# Description: Loop over each pair of indices i, j and compute the sum from k=i to j for A[k]
# Keep the best sum you have found so far.

# @a: Array: some array of integers including at least one positive value
# @n: integer: size of the array  (probably just grab this from A.length or whatever?)
def mssEnumerative(a):
    n = len(a)

    # Return values
    bestSum = -99999999                 # stores the highest MSS found so far
        #TODO: Should we assume it's 0 to start or some big negative number?
    bestSumStartIndex = 0       # stores the index of the starting element of the current best MSS
    bestSumEndIndex = 0         # stores the index of the last element of the current best MSS

    # Enumerating nested loops to calculate best sums so far
    for i in range(0, n):       # start at each element in the array and calculate all sums
        for j in range (i, n):  # Calculate the sum from i to j, for j = i to end of array
            sumCandidate = 0
            for k in range (i, j+1):
                sumCandidate = sumCandidate + a[k]

            if sumCandidate > bestSum:
                bestSum = sumCandidate
                bestSumStartIndex = i
                bestSumEndIndex = j

    return bestSum, bestSumStartIndex, bestSumEndIndex


# Algorithm 2: Better Enumeration
def mssBetterEnumeration(a):
    n = len(a)

    # Return values
    bestSum = -99999999                 # stores the highest MSS found so far
        #TODO: Should we assume it's 0 to start or some big negative number?
    bestSumStartIndex = 0       # stores the index of the starting element of the current best MSS
    bestSumEndIndex = 0         # stores the index of the last element of the current best MSS

    # Enumerating nested loops to calculate best sums so far
    for i in range(0, n):       # start at each element in the array and calculate all sums
        priorSum = 0
        for j in range (i, n):  # Calculate the sum from i to j, for j = i to end of array
            sumCandidate = priorSum + a[j]
            priorSum = sumCandidate

            if sumCandidate > bestSum:
                bestSum = sumCandidate
                bestSumStartIndex = i
                bestSumEndIndex = j

    return bestSum, bestSumStartIndex, bestSumEndIndex



# Function to append output to file
def writeMssTestToFile(a, mssFirst, mssLast, result):
    n = len(a)
    f = open("test.txt", "w")

    # Write original array to file
    writeArray(f, a, 0, n)

    # Write the MSS array to the file
    writeArray(f, a, mssFirst, mssLast)

    # Write result to the file
    f.write(str(result) + "\n\n")

    f.close()

def writeArray(f, a, m, n):
    f.write("[")
    for i in range(m, n - 1):
        f.write(str(a[i]))
        f.write(", ")
    f.write(str(a[n - 1]))
    f.write("]\n")

# Run test on each of the values in the array of inputs
# for v in testValuesRecur:
#     start = timeit.default_timer()
#
#     for i in range(numTests):
#         recursiveFib(v)
#
#     stop = timeit.default_timer()
#     totalTime = stop - start
#     averageTime = totalTime / numTests
#     print(str(v) + "," + str(averageTime))
#
#     f.write(str(v) + "," + str(averageTime) + "\n")
# f.close()




testArray = [1, 4, -9, 8, 1, 3, 3, 1, -1, -4, -6, 2, 8, 19, -10, -11]
expected = 34
result, start, end = mssEnumerative(testArray)
print("testArray: " + str(result) + ".\t Expected: " + str(expected))
print("Start index: " + str(start) + "\tEnd Index: " + str(end))
writeMssTestToFile(testArray, start, end, result)


testArray = [2, 9, 8, 6, 5, -11, 9, -11, 7, 5, -1, -8, -3, 7 -2]
expected = 30
result, start, end = mssEnumerative(testArray)
print("testArray: " + str(result) + ".\t Expected: " + str(expected))
print("Start index: " + str(start) + "\tEnd Index: " + str(end))

testArray = [10, -11, -1, -9, 33, -45, 23, 24, -1, -7 -8, 19]
expected = 50
result, start, end = mssEnumerative(testArray)
print("testArray: " + str(result) + ".\t Expected: " + str(expected))
print("Start index: " + str(start) + "\tEnd Index: " + str(end))

testArray = [31,-41, 59, 26, -53, 58, 97, -93, -23, 84]
expected = 187
result, start, end = mssEnumerative(testArray)
print("testArray: " + str(result) + ".\t Expected: " + str(expected))
print("Start index: " + str(start) + "\tEnd Index: " + str(end))

testArray = [3, 2, 1, 1, -8, 1, 1, 2, 3]
expected = 7
result, start, end = mssEnumerative(testArray)
print("testArray: " + str(result) + ".\t Expected: " + str(expected))
print("Start index: " + str(start) + "\tEnd Index: " + str(end))


testArray = [12, 99, 99, -99, -27, 0, 0, 0, -3, 10]
expected = 210
result, start, end = mssEnumerative(testArray)
print("testArray: " + str(result) + ".\t Expected: " + str(expected))
print("Start index: " + str(start) + "\tEnd Index: " + str(end))


testArray = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
expected = 6
result, start, end = mssEnumerative(testArray)
print("testArray: " + str(result) + ".\t Expected: " + str(expected))
print("Start index: " + str(start) + "\tEnd Index: " + str(end))




# Testing the better enumeration algorithm 2
testArray = [1, 4, -9, 8, 1, 3, 3, 1, -1, -4, -6, 2, 8, 19, -10, -11]
expected = 34
result, start, end = mssBetterEnumeration(testArray)
print("testArray: " + str(result) + ".\t Expected: " + str(expected))
print("Start index: " + str(start) + "\tEnd Index: " + str(end))

testArray = [2, 9, 8, 6, 5, -11, 9, -11, 7, 5, -1, -8, -3, 7 -2]
expected = 30
result, start, end = mssBetterEnumeration(testArray)
print("testArray: " + str(result) + ".\t Expected: " + str(expected))
print("Start index: " + str(start) + "\tEnd Index: " + str(end))

testArray = [10, -11, -1, -9, 33, -45, 23, 24, -1, -7 -8, 19]
expected = 50
result, start, end = mssBetterEnumeration(testArray)
print("testArray: " + str(result) + ".\t Expected: " + str(expected))
print("Start index: " + str(start) + "\tEnd Index: " + str(end))

testArray = [31,-41, 59, 26, -53, 58, 97, -93, -23, 84]
expected = 187
result, start, end = mssBetterEnumeration(testArray)
print("testArray: " + str(result) + ".\t Expected: " + str(expected))
print("Start index: " + str(start) + "\tEnd Index: " + str(end))

testArray = [3, 2, 1, 1, -8, 1, 1, 2, 3]
expected = 7
result, start, end = mssBetterEnumeration(testArray)
print("testArray: " + str(result) + ".\t Expected: " + str(expected))
print("Start index: " + str(start) + "\tEnd Index: " + str(end))


testArray = [12, 99, 99, -99, -27, 0, 0, 0, -3, 10]
expected = 210
result, start, end = mssBetterEnumeration(testArray)
print("testArray: " + str(result) + ".\t Expected: " + str(expected))
print("Start index: " + str(start) + "\tEnd Index: " + str(end))


testArray = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
expected = 6
result, start, end = mssBetterEnumeration(testArray)
print("testArray: " + str(result) + ".\t Expected: " + str(expected))
print("Start index: " + str(start) + "\tEnd Index: " + str(end))