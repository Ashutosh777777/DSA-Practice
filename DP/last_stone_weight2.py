"""
Problem: Last Stone Weight II
Platform: LeetCode
Link: https://leetcode.com/problems/last-stone-weight-ii/
Approach: DP (subset sum → minimize difference)
Time Complexity: O(n * total_sum)
Space Complexity: O(n * total_sum)
"""
class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        total = sum(stones)
        target = total//2
        t = [[False]*(target+1) for _ in range(n+1)]
        for i in range(n+1):
            t[i][0] = True

        for i in range(1, n+1):
            for j in range(target+1):
                if stones[i-1]<=j:
                    t[i][j] = t[i-1][j-stones[i-1]] or t[i-1][j]
                else:
                    t[i][j] = t[i-1][j]
        for k in range(target, -1, -1):
            if t[n][k]:
                return total - k*2

# Convert problem into partitioning stones into two subsets with minimum difference.
# Find subset sum closest to total // 2 using subset sum DP.
# Traverse DP table backward to find maximum achievable sum ≤ target.
# Final answer = total − 2 * chosen_subset_sum.