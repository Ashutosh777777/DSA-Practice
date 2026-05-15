"""
Problem: Container With Most Water
Platform: LeetCode
Link: https://leetcode.com/problems/container-with-most-water/
Approach: Two Pointers / Greedy
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        m = 0

        # Brute Force
        # for i in range(len(height)):
        #     for j in range(i, len(height)):
        #         m = max(
        #             m,
        #             min(height[i], height[j]) * (j - i)
        #         )
        #
        # return m

        i = 0
        j = len(height) - 1

        while i < j:

            m = max(
                m,
                min(height[i], height[j]) * (j - i)
            )

            if height[i] > height[j]:
                j -= 1

            else:
                i += 1

        return m


# Use two pointers starting from both ends of the array.
# Area depends on minimum height and distance between pointers.
# Move the smaller height pointer inward to try finding taller boundary.
# Moving taller pointer cannot improve area with current smaller height.
# Greedy two-pointer approach reduces O(n^2) brute force to O(n).