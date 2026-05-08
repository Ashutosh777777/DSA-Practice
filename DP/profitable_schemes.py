"""
Problem: Profitable Schemes
Platform: LeetCode
Link: https://leetcode.com/problems/profitable-schemes/
Approach: Recursion + Memoization (0/1 Knapsack with People and Profit)
Time Complexity: O(len(group) * n * minProfit)
Space Complexity: O(len(group) * n * minProfit)
"""

class Solution(object):
    def profitableSchemes(self, n, minProfit, group, profit):
        """
        :type n: int
        :type minProfit: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """

        MOD = 10**9 + 7
        memo = {}

        def solve(i, people_used, profit_earned):
            profit_earned = min(profit_earned, minProfit)

            if i == len(group):
                if profit_earned >= minProfit:
                    return 1
                return 0

            if (i, people_used, profit_earned) in memo:
                return memo[(i, people_used, profit_earned)]

            not_take = solve(i + 1, people_used, profit_earned)

            take = 0
            if people_used + group[i] <= n:
                take = solve(
                    i + 1,
                    people_used + group[i],
                    profit_earned + profit[i]
                )

            memo[(i, people_used, profit_earned)] = (take + not_take) % MOD
            return memo[(i, people_used, profit_earned)]

        return solve(0, 0, 0)

# Each crime can either be taken or skipped, so this follows 0/1 knapsack.
# State: (i, people_used, profit_earned) represents current crime index, used people, and profit.
# Cap profit_earned at minProfit because anything above minProfit is already enough.
# If all crimes are processed, count scheme only if profit_earned >= minProfit.
# Use MOD because number of valid schemes can become very large.