# Given two arrays a[] and b[] of size n and m respectively. The task is to find union between these two arrays.

# Union of the two arrays can be defined as the set containing distinct elements from both the arrays. If there are repetitions, then only one occurrence of element should be printed in the union.

# Example 1:
################################################
# Input:
# 5 3
# 1 2 3 4 5
# 1 2 3
# Output: 
# 5
# Explanation: 
# 1, 2, 3, 4 and 5 are the
# elements which comes in the union set
# of both arrays. So count is 5.
################################################


# Example 2:

################################################
# Input:
# 6 2 
# 85 25 1 32 54 6
# 85 2 
# Output: 
# 7
# Explanation: 
# 85, 25, 1, 32, 54, 6, and
# 2 are the elements which comes in the
# union set of both arrays. So count is 7.
################################################

# Your Task:
# Complete doUnion funciton that takes a, n, b, m 
# as parameters and returns the count of union elements of the two arrays. 






arrayA = [85, 25, 1, 32, 54, 6]
arrayB = [85, 2]
unionArray = {}



def doUnion(a,b):
    for i in range(len(a)):
        valueOfA = a[i]
        unionArray[str(valueOfA)] = None
    
    for j in range(len(b)):
        valueOfB = b[j]
        unionArray[str(valueOfB)] = None

    print(len(unionArray))
   
  

doUnion(arrayA, arrayB)
print(unionArray)