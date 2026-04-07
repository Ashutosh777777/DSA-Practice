"""
Problem: 3Sum Closest
Platform: LeetCode
Link: https://leetcode.com/problems/3sum-closest/
Approach: Sorting + Two Pointers
Time Complexity: O(n^2)
Space Complexity: O(1) (excluding sorting)
"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        minD = float('inf')
        ans = 0
        
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            
            while l < r:
                cur = nums[i] + nums[l] + nums[r]
                diff = abs(cur - target)
                
                if diff < minD:
                    minD = diff
                    ans = cur
                
                if cur > target:
                    r -= 1
                elif cur < target:
                    l += 1
                else:
                    return cur
        
        return ans
# Sort the array to enable two-pointer traversal.
# Fix one element and use two pointers to find the best pair for remaining sum.
# Update the closest sum whenever a smaller difference from target is found.
# Move pointers based on comparison with target to get closer to desired sum.