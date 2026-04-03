"""
Problem: Jump Game II
Platform: LeetCode
Link: https://leetcode.com/problems/jump-game-ii/
Approach: Greedy (level-based / BFS range expansion)
Time Complexity: O(n)
Space Complexity: O(1)
"""
from collections import deque
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = r = 0
        res = 0
        while r<len(nums)-1:
            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, i+nums[i])
            l = r+1
            r = farthest
            res+=1
        return res
# Treat the array like levels in BFS, where each range [l, r] represents reachable indices in current jumps.
# For each level, compute the farthest index reachable from all indices in the range.
# Move to the next level by updating l = r + 1 and r = farthest.
# Increment jumps at each level until the last index is reached.