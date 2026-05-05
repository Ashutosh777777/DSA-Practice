"""
Problem: Combination Sum IV
Platform: LeetCode
Link: https://leetcode.com/problems/combination-sum-iv/
Approach: Pure Recursion (Unbounded Knapsack - Order Matters)
Time Complexity: Exponential
Space Complexity: O(target) recursion stack
"""

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def solve(tar):
            if tar == 0:
                return 1
            if tar < 0:
                return 0

            ans = 0
            for num in nums:
                ans += solve(tar - num)

            return ans

        return solve(target)

# Try every number at each step (unbounded choices).
# If target becomes 0 → one valid combination found.
# If target < 0 → invalid path.
# Order matters → (1,2) and (2,1) are different.
# No memoization → recomputes same subproblems many times.