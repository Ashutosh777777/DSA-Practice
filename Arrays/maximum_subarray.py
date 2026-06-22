class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = 0
        m = -1*float('inf')

        for i in nums:
            cur += i
            if cur>m:
                m = cur
            if cur<0:
                cur = 0
        return m