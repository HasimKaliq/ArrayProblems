# # Given an array A of size N of integers. 
# # Your task is to find the minimum 
# # and maximum elements in the array.

# # Example
# Input:
# N = 6
# A[] = {3, 2, 1, 56, 10000, 167}
# Output:
# min = 1, max =  10000

# Your task is to complete the function getMinMax() which takes the array A[] 
# and its size N as inputs and returns the minimum and maximum element of the array.


## The time complexity of this program runs in O(N)
# if this was alrady sorted the returing only the index 1 and index n-1 would 
# produce the output of the min and the max in O(1) Times
# The running time of this algorithn would then be dependant on the run time of what
# sorting algorithm was used to sort. Since non was used here we have O(n) or Theta(n)
arr = [3, 2, 1, 56, 10000, 167]
sizeOfArray = len(arr)

# A --> Array
# N --> Size of the array A
def getMinMax(A, N):
    tempMin = A[0]
    tempMax = A[1]
    
    for i in range(N):
       
        if(A[i] > tempMax):
            tempMax = A[i]
        if(A[i] < tempMin):
            tempMin = A[i]
    return tempMin, tempMax

print( getMinMax(arr, sizeOfArray) )
