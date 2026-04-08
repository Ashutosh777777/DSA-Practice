"""
Problem: Merge Sorted Array
Platform: LeetCode
Link: https://leetcode.com/problems/merge-sorted-array/
Approach: Two pointers (merge from the end)
Time Complexity: O(m + n)
Space Complexity: O(1)
"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        prevRows = self.generate(numRows - 1)
        newRow = [1] * numRows
        
        for i in range(1, numRows - 1):
            newRow[i] = prevRows[-1][i - 1] + prevRows[-1][i]
        
        prevRows.append(newRow)
        return prevRows
# Use three pointers starting from the end of both arrays.
# Compare elements from nums1 and nums2, placing the larger one at the back.
# Decrement pointers accordingly and fill nums1 from right to left.
# If nums2 still has elements, copy them (nums1 leftovers are already in place).