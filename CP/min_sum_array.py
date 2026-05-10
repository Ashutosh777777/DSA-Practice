"""
Problem: Minimum Array Sum
Platform: LeetCode
Link: 
Approach: Sieve / Smallest Divisor Precomputation
Time Complexity: O(n + m log m)
Space Complexity: O(m)
"""

class Solution(object):
    def minArraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        mx = max(nums)

        present = [False] * (mx + 1)

        for x in nums:
            present[x] = True

        best = [0] * (mx + 1)

        for d in range(1, mx + 1):

            if present[d]:

                for m in range(d, mx + 1, d):

                    if best[m] == 0:
                        best[m] = d

        ans = 0

        for x in nums:
            ans += best[x]

        return ans


# Mark all numbers present in the array.
# For every present divisor d, visit all its multiples.
# Store the first valid divisor for each multiple in best[].
# best[x] represents the smallest present divisor of x.
# Sum the smallest valid divisor for every array element.
# Uses sieve-style traversal for efficient divisor processing.