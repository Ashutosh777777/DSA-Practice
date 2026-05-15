"""
Problem: Combination Sum
Platform: LeetCode
Link: https://leetcode.com/problems/combination-sum/
Approach: Backtracking / Unbounded Knapsack Pattern
Time Complexity: O(2^target)
Space Complexity: O(target)
"""

class Solution(object):

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        cur = []
        res = []

        def solve(i, rem):

            if rem == 0:
                res.append(cur[:])
                return

            if rem < 0 or i == len(candidates):
                return

            # Take current element
            cur.append(candidates[i])

            solve(i, rem - candidates[i])

            cur.pop()

            # Skip current element
            solve(i + 1, rem)

        solve(0, target)

        return res


# This problem follows the Unbounded Knapsack pattern.
# At every index, either take or skip the current candidate.
# If taken → stay at same index because reuse is allowed.
# If skipped → move to next index.
# When remaining target becomes 0 → store current combination.
# Backtracking removes the last chosen element after recursion.