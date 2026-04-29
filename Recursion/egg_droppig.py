"""
Problem: Super Egg Drop
Platform: LeetCode
Link: https://leetcode.com/problems/super-egg-drop/
Approach: Recursion by trying every floor and taking worst case
Time Complexity: Exponential
Space Complexity: O(n) recursion stack
"""

class Solution(object):
    def superEggDrop(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """

        def solve(e, f):
            if f == 0 or f == 1:
                return f

            if e == 1:
                return f

            mini = float('inf')

            for i in range(1, f + 1):
                temp = 1 + max(solve(e - 1, i - 1), solve(e, f - i))
                mini = min(temp, mini)

            return mini

        return solve(k, n)

# Try dropping an egg from every floor from 1 to f.
# If egg breaks, search below with one less egg: solve(e - 1, i - 1).
# If egg does not break, search above with same eggs: solve(e, f - i).
# Take worst case using max(), then minimize attempts using min().