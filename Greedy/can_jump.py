"""
Problem: Jump Game
Platform: LeetCode
Link: https://leetcode.com/problems/jump-game/
Approach: Greedy (track maximum reachable index)
Time Complexity: O(n) single pass
Space Complexity: O(1)
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxi = 0
        for i in range(len(nums)-1):
            if i>maxi:
                return False
            maxi = max(maxi, i+nums[i])
        return (maxi>=(len(nums)-1))

# Maintain a variable maxi to track the farthest reachable index so far.
# Traverse the array and check if the current index is reachable (i <= maxi).
# Update maxi = max(maxi, i + nums[i]) at each step.
# If traversal completes and maxi reaches the last index, return True; otherwise False.