"""
Problem: Find the Substring With Maximum Cost
Platform: LeetCode
Link: https://leetcode.com/problems/find-the-substring-with-maximum-cost/
Approach: Hash Map / Kadane's Algorithm
Time Complexity: O(n + k)
Space Complexity: O(n + k)
"""

from typing import List

class Solution:

    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:

        def max_sum_sub(arr):

            m = 0

            c = 0

            i = 0

            while i < len(arr):

                c += arr[i]

                m = max(m, c)

                i += 1

                if c < 0:
                    c = 0

            return m

        m = {}

        arr = []

        for i in range(len(chars)):
            m[chars[i]] = vals[i]

        for i in range(len(s)):

            if s[i] in m:
                arr.append(m[s[i]])

            else:
                arr.append(ord(s[i]) - 96)

        return max_sum_sub(arr)


# Store custom character values in a hash map.
# If a character exists in chars, use its custom value from vals.
# Otherwise, use its default alphabet value: a = 1, b = 2, ..., z = 26.
# Convert the string into an array of integer costs.
# Now the problem becomes maximum subarray sum.
# Use Kadane's Algorithm to find the maximum cost substring.
# If the running sum becomes negative, reset it to 0.
# Return the maximum sum found.