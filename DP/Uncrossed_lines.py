"""
Problem: Uncrossed Lines
Platform: LeetCode
Link: https://leetcode.com/problems/uncrossed-lines/
Approach: Dynamic Programming (Longest Common Subsequence pattern)
Time Complexity: O(n * m)
Space Complexity: O(n * m)
"""

class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """

# Recursive
        # def solve(nums1, nums2):
        n = len(nums1)
        m = len(nums2)

        #     if n == 0 or m == 0:
        #         return 0
            
        #     if nums1[-1] == nums2[-1]:
        #         return 1 + solve(nums1[:n-1], nums2[:m-1])
        #     else:
        #         return max(
        #             solve(nums1[:n-1], nums2[:]),
        #             solve(nums1[:], nums2[:m-1])
        #         )
        # return solve(nums1, nums2)

# DP
        t = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):

                if nums1[i - 1] == nums2[j - 1]:
                    t[i][j] = 1 + t[i - 1][j - 1]

                else:
                    t[i][j] = max(t[i - 1][j], t[i][j - 1])

        return t[n][m]


# This problem is identical to the Longest Common Subsequence (LCS) pattern.
# t[i][j] stores the maximum uncrossed lines using first i and j elements.
# If elements match → take diagonal value + 1.
# Otherwise → take maximum of top and left cell.
# Extra row and column handle base cases when one array is empty.