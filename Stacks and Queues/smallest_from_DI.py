"""
Problem: Construct Smallest Number From DI String
Platform: LeetCode
Link: https://leetcode.com/problems/construct-smallest-number-from-di-string/
Approach: Stack / Greedy
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:

    def smallestNumber(self, pattern: str) -> str:

        stack = []

        count = 1

        num = ""

        pattern += "O"

        for c in pattern:

            stack.append(count)

            count += 1

            if c == "I" or c == "O":

                while stack:
                    num += str(stack.pop())

        return num


# Use numbers starting from 1 to build the smallest valid number.
# Use a stack to handle decreasing sequences.
# Keep pushing numbers into the stack while traversing the pattern.
# When an 'I' is found, pop all values from the stack and add them to num.
# This reverses the previous decreasing section correctly.
# Add an extra dummy character 'O' at the end to empty the remaining stack.
# The stack ensures that every 'D' sequence gets reversed in the final number.
# Return num as the smallest number that follows the given pattern.