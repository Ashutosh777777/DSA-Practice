"""
Problem: Merge Sorted Array
Platform: LeetCode
Link: https://leetcode.com/problems/merge-sorted-array/
Approach: Two pointers (merge from the end)
Time Complexity: O(m + n)
Space Complexity: O(1)
"""
from collections import deque
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1      
        k = m + n - 1  
        
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
# Use three pointers starting from the end of both arrays.
# Compare elements from nums1 and nums2, placing the larger one at the back.
# Decrement pointers accordingly and fill nums1 from right to left.
# If nums2 still has elements, copy them (nums1 leftovers are already in place).