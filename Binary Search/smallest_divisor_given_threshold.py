class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        def possible(mid):
            totol = 0
            for i in nums:
                totol += ((i+mid-1)//mid)
            return totol<=threshold
        s = 1
        e = sum(nums)

        while s<=e:
            mid = (s+e)//2
            if possible(mid):
                e = mid - 1
            else:
                s = mid + 1
        return s