# An element is called a peak element 
# if its value is not smaller than the 
# value of its adjacent elements(if they exists).
# Given an array arr[] of size N, 
# find the index of any one of its peak elements.
# Note: The generated output will always be 1 
# if the index that you return is correct. Otherwise output will be 0. 

# Example
# Input:
# N = 3
# arr[] = {1,2,3}
# Output: 2
# Explanation: index 2 is 3.
# It is the peak element as it is 
# greater than its neighbour 2.

# But the downside to the algorithm is it's time complexity is in the order of n  -> O(n)
# But it can be solved in O(log N) times
arr = [10, 4, 53, 52, 42, 5, 64, 6, 2] # works for unsorted value
#arr = [1, 2, 4, 5, 6] # works for sorted values
sizeOfArray = len(arr)
peakValue = 0
temp = 0
for i in range(sizeOfArray - 1):
    if(arr[i] > arr[i + 1]):
        temp = arr[i]
    
    if(arr[i] < arr[i + 1]):
        temp = arr[i + 1]
    
    if( temp > peakValue):
        peakValue = temp

print(arr.index(peakValue))
