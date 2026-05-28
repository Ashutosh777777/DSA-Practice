"""
Problem: Largest Number
Platform: LeetCode
Link: https://leetcode.com/problems/largest-number/
Approach: Custom Sorting / Comparator
Time Complexity: O(n log n)
Space Complexity: O(n)
"""

from functools import cmp_to_key

class Solution:

    def largestNumber(self, nums: List[int]) -> str:

        nums = list(map(str, nums))

        def compare(a, b):

            if a + b > b + a:
                return -1

            elif b + a > a + b:
                return 1

            else:
                return 0

        nums.sort(key=cmp_to_key(compare))

        ans = ''.join(nums)

        if ans[0] == '0':
            return '0'

        return ans


# Convert numbers to strings to compare concatenated orders.
# For two strings a and b, compare a+b with b+a.
# Put a before b if a+b creates a larger number.
# Custom comparator arranges numbers in best possible order.
# If final answer starts with 0, all numbers are 0 → return "0".