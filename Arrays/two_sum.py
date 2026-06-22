class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}
        for i in range(len(nums)):
            if target - nums[i] in m:
                return [m[target-nums[i]], i]
            m[nums[i]] = i
        