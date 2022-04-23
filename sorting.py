# # Given a random set of numbers, Print them in sorted order.

# Input:
# N = 4
# arr[] = {1, 5, 3, 2}
# Output: {1, 2, 3, 5}
# Explanation: After sorting array will 
# be like {1, 2, 3, 5}.

# Your task is to complete the function sortArr() 
# which takes the list of integers and the size N as inputs 
# and returns the modified list.

# Expected Time Complexity: O(N * log N)
# Expected Auxiliary Space: O(1)

# Constraints:
# 1 ≤ N, A[i] ≤ 105


# An approach that only worked for when the array was less than or equal to 4
#   temp = 0
#     for i in range(N-1):
#         if(A[i] > A[i+1]):
#             temp = A[i+1] 
#             A[i+1] = A[i] 
#             A[i] = temp

#     for j in range(N-1):
#         if(A[j] > A[j+1]):
#             temp = A[j+1] 
#             A[j+1] = A[i] 
#             A[i] = temp
#     return A

# use nested loops to solve it
# This Alhamdullahi was solved in the time complexity being O(n^2)
# Best Case Time Complexity: O(n). The best-case occurs when an array is already sorted

# Driver code to test below
arr = [64, 34, 25, 12, 22, 11, 90]
lengthOfArray = len(arr)
def sortArr(A, N):
   temp = 0
   for i in range(len(arr) - 1):
     for i in range(len(arr) - 1):
        temp = arr[i]
        if(arr[i+1] < temp):
           temp = arr[i+1]
           arr[i+1] = arr[i]
           arr[i] = temp
           temp = 0
   return A

print(sortArr(arr, lengthOfArray))

