"""
Problem: Maximum Product Subarray
Platform: LeetCode
Link: https://leetcode.com/problems/maximum-product-subarray/
Approach: Dynamic Programming / Track Maximum and Minimum Product
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # MCM-style recursion idea does not fit well here
        # because subarray product depends on continuous prefix/suffix products.

        if not nums:
            return 0

        Max = nums[0]
        Min = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):

            num = nums[i]

            if num < 0:
                Max, Min = Min, Max

            Max = max(num, num * Max)
            Min = min(num, num * Min)

            ans = max(ans, Max)

        return ans


# Keep both maximum and minimum product ending at current index.
# Minimum is needed because negative number can turn it into maximum.
# If current number is negative → swap Max and Min.
# Either start new subarray from current number or extend previous one.
# Update answer with the best maximum product found so far.