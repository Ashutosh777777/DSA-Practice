"""
Problem: Matrix Chain Multiplication
Platform: GFG
Link: https://www.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1
Approach: Recursion (partition at every possible k)
Time Complexity: Exponential
Space Complexity: O(n) recursion stack
"""
class Solution:
    def matrixMultiplication(self, arr):
        # code here
        n = len(arr)
        i = 1
        j = n-1
        
        def solve(arr, i, j):
            if i>=j:
                return 0
            m = float('inf')
            for k in range(i, j):
                
                temp = solve(arr, i, k) + solve(arr, k+1, j) + arr[i-1]*arr[k]*arr[j]
            
            m = min(m, temp)
            return m
        return solve(arr, 1, n-1)
# Recursively try every possible partition point k between i and j.
# Compute cost of left part, right part, and multiplying the two resulting matrices.
# Take the minimum cost among all possible partitions.
# Base case: if chain has one matrix or less (i >= j), cost is 0.