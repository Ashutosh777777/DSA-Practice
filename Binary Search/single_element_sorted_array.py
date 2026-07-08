class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        s = 0
        e = n - 1
        while s<=e:
            m = s + (e-s)//2
            if ((m-1<0 or nums[m]!=nums[m-1]) and (m+1==n or nums[m]!=nums[m+1])):
                return nums[m]
            left = (m-1) if nums[m]==nums[m-1] else m
            if left%2:
                e = m-1
            else:
                s = m+1
            
