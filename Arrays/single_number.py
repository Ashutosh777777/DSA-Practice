from itertools import islice
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] not in islice(nums, 0, i) and nums[i] not in islice(nums, i+1, len(nums)):
                return nums[i]
        