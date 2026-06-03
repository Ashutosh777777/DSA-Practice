"""
Problem: Daily Temperatures
Platform: LeetCode
Link: https://leetcode.com/problems/daily-temperatures/
Approach: Monotonic Stack
Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = [len(temperatures) - 1]

        t = temperatures[:]

        res = []

        for j in range(len(t) - 1, -1, -1):

            while stack and t[j] >= t[stack[-1]]:
                stack.pop()

            if not stack:
                res.append(0)

            else:
                res.append(stack[-1] - j)

            stack.append(j)

        return res[::-1]


# Traverse the temperatures array from right to left.
# Use a monotonic stack to store indices of warmer future days.
# While the current temperature is greater than or equal to the temperature
# at the index on top of the stack, pop from the stack.
# If the stack becomes empty, there is no warmer day ahead, so append 0.
# Otherwise, the top of the stack gives the nearest warmer day.
# Store the difference between indices as the waiting days.
# Reverse the result at the end because answers were added from right to left.