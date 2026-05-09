"""
Problem: Subarray with Given Sum
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1
Approach: Sliding Window / Two Pointers
Time Complexity: O(n)
Space Complexity: O(1)
"""

# User function Template for python3

class Solution:
    def subarraySum(self, arr, target):
        # code here

        i = 0
        cur = 0

        for j in range(len(arr)):

            cur += arr[j]

            while cur > target and i <= j:
                cur -= arr[i]
                i += 1

            if cur == target:
                return [i + 1, j + 1]

        return [-1]


# Maintain a sliding window using two pointers i and j.
# Expand window by adding arr[j] to current sum.
# If sum becomes greater than target → shrink window from left.
# When current sum equals target → return 1-based indices.
# Works because all array elements are positive.