"""
Problem: Find Unique Element
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/finding-the-numbers0215/1
Approach: Sorting + Pair Checking
Time Complexity: O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def findUnique(self, arr):
        # code here

        arr.sort()

        arr.append(-1)

        for i in range(0, len(arr), 2):

            if arr[i] != arr[i + 1]:
                return arr[i]


# Sort the array so duplicate elements become adjacent.
# Traverse array in pairs of two indices at a time.
# If a pair is unequal → current element is unique.
# Extra -1 avoids index out of range for the last element.
# Works because every other element appears exactly twice.