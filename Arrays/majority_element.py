class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m = {}
        l = len(nums)
        for i in range(l):
            if nums[i] not in m:
                m[nums[i]] = 1
            else:
                m[nums[i]] += 1
        res = []
        for key, value in m.items():
            if value>l//3:
                res.append(key)
        return res