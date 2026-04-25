"""
Problem: Valid Digit Check
Approach: Convert number to string and check if digit x exists but is not the first digit
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def validDigit(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: bool
        """
        n = str(n)

        if str(x) in n and n[0] != str(x):
            return True

        return False


# Convert n into string so digit comparison becomes easy.
# Check if digit x is present anywhere inside the number.
# Ensure x is not the first digit by comparing with n[0].
# Return True only when both conditions are satisfied, otherwise False.