"""
Problem: Uncrossed Lines
Platform: LeetCode
Link: https://leetcode.com/problems/uncrossed-lines/
Approach: Recursion (Longest Common Subsequence pattern)
Time Complexity: O(2^(n+m))
"""

class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """

        def solve(nums1, nums2):
            n = len(nums1)
            m = len(nums2)

            if n == 0 or m == 0:
                return 0
            
            if nums1[-1] == nums2[-1]:
                return 1 + solve(nums1[:n-1], nums2[:m-1])
            else:
                return max(
                    solve(nums1[:n-1], nums2[:]),
                    solve(nums1[:], nums2[:m-1])
                )

        return solve(nums1, nums2)


# This problem follows the Longest Common Subsequence (LCS) pattern.
# If the last elements match → include that line and move both pointers.
# Otherwise → try skipping one element from either array and take maximum.
# Base case: if either array becomes empty → return 0.
# Pure recursion explores all possibilities, causing exponential complexity.