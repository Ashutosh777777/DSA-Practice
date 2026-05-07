"""
Problem: Guess Number Higher or Lower II
Platform: LeetCode
Link: https://leetcode.com/problems/guess-number-higher-or-lower-ii/
Approach: Recursion + Memoization (Minimax DP)
Time Complexity: O(n^3)
Space Complexity: O(n^2)
"""

class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """

        memo = {}

        def solve(start, end):
            if start >= end:
                return 0

            if (start, end) in memo:
                return memo[(start, end)]

            ans = float('inf')

            for guess in range(start, end + 1):

                left = solve(start, guess - 1)
                right = solve(guess + 1, end)

                cost = guess + max(left, right)

                ans = min(ans, cost)

            memo[(start, end)] = ans
            return ans

        return solve(1, n)

# Try every number as the current guess within range [start, end].
# If guess is wrong, worst case comes from larger of left or right range.
# Add current guessed number to total cost.
# Choose minimum cost among all possible guesses.
# Memoization stores answer for each (start, end) range.