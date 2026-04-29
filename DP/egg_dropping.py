"""
Problem: Super Egg Drop
Platform: LeetCode
Link: https://leetcode.com/problems/super-egg-drop/
Approach: Memoization + Binary Search Optimization
Time Complexity: O(k * n * log n)
Space Complexity: O(k * n)
"""

class Solution(object):
    def superEggDrop(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """

        t = [[-1] * (n + 1) for _ in range(k + 1)]

        def solve(e, f):
            if f == 0 or f == 1:
                return f

            if e == 1:
                return f

            if t[e][f] != -1:
                return t[e][f]

            low, high = 1, f
            mini = float('inf')

            while low <= high:
                mid = (low + high) // 2

                left = solve(e - 1, mid - 1)
                right = solve(e, f - mid)

                temp = 1 + max(left, right)
                mini = min(mini, temp)

                if left < right:
                    low = mid + 1
                else:
                    high = mid - 1

            t[e][f] = mini
            return mini

        return solve(k, n)

# Use DP table t[e][f] to store minimum attempts for e eggs and f floors.
# Binary search is used because left side increases and right side decreases.
# If egg breaks → search below, else → search above with same eggs.
# Take worst case using max(), then minimize attempts using binary search.