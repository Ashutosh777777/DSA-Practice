"""
Problem: Count Frequency of Array Elements
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/1
Approach: Hash Map / Dictionary Counting
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def countFreq(self, arr):
        # code here

        res = []
        t = {}

        for num in arr:

            if num not in t:
                t[num] = 1

            else:
                t[num] += 1

        for key, value in t.items():
            res.append([key, value])

        return res


# Use a dictionary to store frequency of each element.
# Traverse array and increase count for every occurrence.
# Store result as [element, frequency] pairs in a list.
# Hash map allows insertion and lookup in O(1) average time.