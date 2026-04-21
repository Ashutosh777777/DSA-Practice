"""
Problem: Matrix Chain Multiplication
Platform: GFG
Link: https://www.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1
Approach: Recursion + Memoization (DP) with partition at every k
Time Complexity: O(n^3)
Space Complexity: O(n^2) + O(n) recursion stack
"""
class Solution:
    def matrixMultiplication(self, arr):
        n = len(arr)
        
        t = [[-1]*(n+1) for i in range(n+1)]
        
        def solve(arr, i, j):
            if i>=j:
                return 0
            if t[i][j]!=-1:
                return t[i][j]
            
            mini = float('inf')
            for k in range(i, j):
                temp = solve(arr, i, k) + solve(arr, k+1, j) + arr[i-1]*arr[k]*arr[j]
                mini = min(mini, temp)
            t[i][j] = mini
            return mini
        return solve(arr, 1, n-1)

# Try all partition points k and take minimum multiplication cost.
# Memoization avoids recomputing overlapping subproblems.
# Cost formula: arr[i-1] * arr[k] * arr[j] for current partition.
# Converts exponential recursion into O(n^3) DP solution.