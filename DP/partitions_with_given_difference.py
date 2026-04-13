"""
Problem: Count Partitions with Given Difference
Platform: GFG
Link: https://www.geeksforgeeks.org/problems/count-of-subsets-with-given-difference/1
Approach: Dynamic Programming (count subset sum transformation)
Time Complexity: O(n * target)
Space Complexity: O(n * target)
"""
class Solution:
    def countPartitions(self, arr, diff):
        # code here
        if (sum(arr)+diff)%2!=0:
            return 0
        target = (sum(arr)+diff)//2
        
        n = len(arr)
        t = [[0]*(target+1) for _ in range(n+1)]
        for i in range(n+1):
            
            t[i][0] = 1
        for i in range(1, n+1):
            for j in range(target+1):
                if arr[i-1] <= j:
                    t[i][j] = t[i-1][j] + t[i-1][j-arr[i-1]]
                else:
                    t[i][j] = t[i-1][j]
        return t[n][target]
# Convert partition problem into subset sum: find subsets with sum = (sum + diff) / 2.
# If (sum + diff) is odd, no valid partition exists.
# Use DP where dp[i][j] stores count of subsets using first i elements forming sum j.
# Transition: include + exclude → add both counts.