"""
Problem: Rod Cutting
Platform: GFG
Link: https://www.geeksforgeeks.org/problems/rod-cutting0840/1
Approach: Dynamic Programming (Unbounded Knapsack)
Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""

#User function Template for python3

class Solution:
    def cutRod(self, price):
        #code here
        n = len(price)
        wt = [i for i in range(1, n+1)]
        t = [[0]*(n+1) for _ in range(n+1)]\
        
        for i in range(n+1):
            for j in range(n+1):
                
                if wt[i-1]<=j:
                    t[i][j] = max(price[i-1]+t[i][j-wt[i-1]], t[i-1][j])
                else:
                    t[i][j] = t[i-1][j]
        return t[n][n]
                    
# Treat rod lengths as weights and prices as values.
# Since we can reuse lengths multiple times → unbounded knapsack.
# Either cut the rod (take same length again) or skip it.
# Maximize total value for rod length n.