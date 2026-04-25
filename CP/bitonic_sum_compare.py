"""
Problem: Compare Bitonic Sums
Approach: Find the maximum element (peak) and compare increasing and decreasing part sums
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def compareBitonicSums(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = sum(nums[:nums.index(max(nums)) + 1])
        d = sum(nums[nums.index(max(nums)):])

        if i > d:
            return 0
        elif i < d:
            return 1

        return -1


# Find the peak element using max(nums) and its index.
# Calculate left sum including the peak as increasing part.
# Calculate right sum including the peak as decreasing part.
# Return 0 if left sum is greater, 1 if right sum is greater, else -1.