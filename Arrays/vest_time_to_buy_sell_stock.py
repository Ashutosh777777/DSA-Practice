class Solution(object):
    def maxProfit(self, nums):
        """
        :type prices: List[int]
        :rtype: int
        """
        m = float('inf')
        M = 0

        for i in range(len(nums)):
            m = min(m, nums[i])
            M = max(M, nums[i] - m)
        return M