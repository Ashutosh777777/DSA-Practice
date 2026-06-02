"""
Problem: Count Pairs Whose Sum is Less than Target
Platform: LeetCode
Link: https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/
Approach: Sorting / Two Pointers
Time Complexity: O(n log n)
Space Complexity: O(1)
"""

from typing import List

class Solution:

    def countPairs(self, nums: List[int], target: int) -> int:

        nums.sort()

        left = 0
        right = len(nums) - 1

        count = 0

        while left < right:

            if nums[left] + nums[right] < target:
                count += right - left
                left += 1

            else:
                right -= 1

        return count


# Sort the array first.
# Use two pointers: one at the start and one at the end.
# If nums[left] + nums[right] is less than target,
# then all pairs from left to right are valid with nums[left].
# Add right - left to count and move left forward.
# If the sum is greater than or equal to target,
# move right backward to reduce the sum.
# Return the total number of valid pairs.