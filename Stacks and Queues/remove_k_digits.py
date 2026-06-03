"""
Problem: Remove K Digits
Platform: LeetCode
Link: https://leetcode.com/problems/remove-k-digits/
Approach: Monotonic Stack / Greedy
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:

    def removeKdigits(self, num: str, k: int) -> str:

        stack = []

        for n in num:

            while stack and n < stack[-1] and k > 0:
                stack.pop()
                k -= 1

            stack.append(n)

        while k > 0 and stack:
            stack.pop()
            k -= 1

        res = ''.join(stack).lstrip('0')

        if res == "":
            return "0"

        return res


# Use a monotonic increasing stack to build the smallest possible number.
# Traverse each digit of num one by one.
# If the current digit is smaller than the top of the stack,
# remove the larger digit from the stack while k removals are still available.
# This helps place smaller digits earlier in the final number.
# After traversal, if k is still greater than 0, remove digits from the end.
# Join the stack to form the final number.
# Remove leading zeroes using lstrip('0').
# If the result becomes empty, return "0".
# Otherwise, return the final result.