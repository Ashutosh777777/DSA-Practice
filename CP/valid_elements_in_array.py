"""
Problem: Valid Elements in an Array
Platform: LeetCode
Link: Weekly Contest 499 - Q1
Approach: Prefix Maximum + Suffix Maximum Boolean Tracking
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def findValidElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        max1 = -float('inf')
        max2 = -float('inf')

        res1 = []
        res2 = []
        res = []

        n = len(nums)

        for i in range(n):
            if nums[i] > max1:
                max1 = nums[i]
                res1.append(True)
            else:
                res1.append(False)

        for j in range(n - 1, -1, -1):
            if nums[j] > max2:
                max2 = nums[j]
                res2.append(True)
            else:
                res2.append(False)

        res2 = res2[::-1]

        for k in range(n):
            if res1[k] or res2[k]:
                res.append(nums[k])

        return res


# Traverse from left to right and mark elements greater than all previous elements.
# Traverse from right to left and mark elements greater than all elements on the right.
# Reverse the right-side boolean array to match original indices.
# If either left-check or right-check is true, include that element in answer.