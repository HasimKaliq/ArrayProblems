# Given a vector of N positive integers and an integer X. 
# The task is to find the frequency of X in vector.


# Input:
# N = 5
# vector = {1, 1, 1, 1, 1}
# X = 1
# Output: 
# 5
# Explanation: Frequency of 1 is 5.


# Your Task:
# Your task is to complete the function findFrequency() which should count the frequency of X and return it.

# Bismillahi Rahmani Rahim
# Time complexity because i have to check every element using a linear search here cause --> O(n)
def findFrequency():
    frequencyFound = 0
    frequenyOfNumber = int(input("Enter the number you would like to know it's frequency to: "))
    vector = [1, 3, 1, 5, 1]
    for i in range(len(vector)):
        if(vector[i] == frequenyOfNumber):
            frequencyFound+=1
    return frequencyFound


print(findFrequency())

