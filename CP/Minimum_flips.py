"""
Problem: Minimum Flips
Platform: LeetCode
Link: 
Approach: Case Analysis / Counting
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def minFlips(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)

        o = s.count("1")
        z = n - o

        a = max(0, o - 1)

        b = z

        c = float('inf')
        if n >= 2:
            mid = s[1:n-1].count("1")
            l = 1 if s[0] == "0" else 0
            r = 1 if s[n-1] == "0" else 0
            c = l + mid + r

        return min(a, b, c)


# Count total 1s and 0s in the string.
# Case a: keep at most one '1', flip extra 1s.
# Case b: convert all characters to '1' by flipping all 0s.
# Case c: keep boundary characters as '1' and make middle mostly 0.
# Return the minimum flips among all valid cases.