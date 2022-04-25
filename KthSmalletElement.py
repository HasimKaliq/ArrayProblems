# Given an array arr[] and an integer K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.

# Example 1:

# Input:
# N = 6
# arr[] = 7 10 4 3 20 15
# K = 3
# Output : 7
# Explanation :
# 3rd smallest element in the given 
# array is 7.
# Example 2:

# Input:
# N = 5
# arr[] = 7 10 4 20 15
# K = 4
# Output : 15
# Explanation :
# 4th smallest element in the given 
# array is 15.


# Your task is to complete the function kthSmallest() 
# which takes the array arr[], integers l and r denoting the starting a
# nd ending index of the array
#  and an integer K as input and returns the Kth smallest element.

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(log(n))
# Constraints:
# 1 <= N <= 105
# 1 <= arr[i] <= 105
# 1 <= K <= N

# Bismillah-ir Rahman-ir Rahim
# This is a sorting problem, all we have to do is sort the array
# then make use of a hack by reducing K by 1
# e.g find the 3 smallest number in the array of [3, 5, 2, 1]
# once sorted we have [1, 2, 5, 3], the 3 smallest is 5
# but if we index the array using 3 we get the value 3 as 3rd smallest which is wrong
# but by reducing 3-1 = 2 and once 2 is used to index the array we get 5 --> Correct. (¬‿¬)


# the only problem left is which sorting algorithm to pick we have these constraints
# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(log(n))

# i cant really translate this question but i think, the sorting algorithm does not matter much
# as long as once sorted it cause O(log(n))
# and once traversing the array it should cause O(n) i could be wrong
# because i dont know any sorting algorithm that runs in O(n)

# i choose the insertion sort beacuse i dont know it, and it's time complexities appeal to me
# - Worst Case O(n2)
# - Best Case O(n)
# - Space Complexity O(1)

# Insertion sort in Python


def kthSmallest(array, K, N):

    for step in range(1, N):
        key = array[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key
    print(f' The {K}th smallest element is {array[K-1]}')


data = [7, 10, 4, 20, 15]
N = len(data)
K = int(input("Enter the number of the smallest element you desire: "))
kthSmallest(data, K, N)
  

