"""
Problem: House Robber II
Platform: LeetCode
Link: https://leetcode.com/problems/house-robber-ii/
Approach: DP (Include/Exclude) + Circular Handling
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def simple_rob(nums):
            rob, not_rob = 0, 0
            for num in nums:
                rob, not_rob = not_rob + num, max(rob, not_rob)
            return max(rob, not_rob)

        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            return max(simple_rob(nums[1:]), simple_rob(nums[:-1]))

# Houses are in a circle → first and last cannot both be robbed.
# Break into two cases: exclude first OR exclude last house.
# simple_rob uses two variables:
#   rob → max money if current house is robbed
#   not_rob → max money if current house is skipped
# At each step, choose best option without adjacent conflicts.