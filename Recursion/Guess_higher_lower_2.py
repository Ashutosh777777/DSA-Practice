"""
Problem: Guess Number Higher or Lower II
Platform: LeetCode
Link: https://leetcode.com/problems/guess-number-higher-or-lower-ii/
Approach: Pure Recursion / Minimax Strategy
Time Complexity: Exponential
Space Complexity: O(n) recursion stack
"""

class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """

        nums = [i + 1 for i in range(n)]

        def solve(nums):
            if len(nums) <= 1:
                return 0

            ans = float('inf')

            for i in range(len(nums)):
                temp = nums[i] + max(
                    solve(nums[:i]),
                    solve(nums[i + 1:])
                )

                ans = min(temp, ans)

            return ans

        return solve(nums)

# Try every number as the current guess.
# If guess is wrong, worst case cost comes from larger side.
# Use max(left, right) because opponent can force worst case.
# Add current guessed number to total cost.
# Choose minimum among all possible guesses.
# No memoization → overlapping subproblems cause exponential complexity.