"""
Problem: Combination Sum IV
Platform: LeetCode
Link: https://leetcode.com/problems/combination-sum-iv/
Approach: Recursion + Memoization (Unbounded Knapsack - Order Matters)
Time Complexity: O(target * len(nums))
Space Complexity: O(target)
"""

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        t = [-1] * (target + 1)

        def solve(tar):
            if tar == 0:
                return 1
            if tar < 0:
                return 0

            if t[tar] != -1:
                return t[tar]

            ans = 0
            for num in nums:
                ans += solve(tar - num)

            t[tar] = ans
            return ans

        return solve(target)

# Unbounded choices: can use each number multiple times.
# Order matters → permutations are counted as different.
# DP state: t[tar] = number of ways to form target = tar.
# For each tar, try all nums and reduce target.
# Memoization avoids recomputing same target values.