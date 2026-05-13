"""
Problem: Majority Element
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/majority-element-1587115620/1
Approach: Hash Map / Frequency Counting
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:

    def majorityElement(self, arr):

        n = len(arr)
        t = {}

        for i in range(n):

            if arr[i] in t:
                t[arr[i]] += 1

            else:
                t[arr[i]] = 1

        for element, count in t.items():

            if count > n // 2:
                return element

        return -1


# Count frequency of every element using a dictionary.
# Traverse the array and update occurrence count.
# Majority element appears more than n // 2 times.
# Return the element whose frequency exceeds this limit.
# If no such element exists → return -1.