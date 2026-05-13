"""
Problem: Maximum Sum Without Adjacent Elements
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/max-sum-without-adjacents2430/1
Approach: Recursion + Memoization (House Robber pattern)
Time Complexity: O(n)
Space Complexity: O(n)
"""

# User function Template for python3

class Solution:

    def findMaxSum(self, arr):
        # code here

        t = {}
        n = len(arr)

        def solve(i):

            if i in t:
                return t[i]

            if i >= n:
                return 0

            t[i] = max(
                arr[i] + solve(i + 2),
                solve(i + 1)
            )

            return t[i]

        return solve(0)


# At every index, either take current element or skip it.
# If taken → move to i + 2 to avoid adjacent selection.
# If skipped → move to next index.
# Memoization stores answers for already solved indices.
# This follows the classic House Robber DP pattern.