from itertools import islice
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        n = len(nums)
        # for i in range(n):
        #     for j in range(i, n):
        #         if sum(islice(nums, i, j+1))==k:
        #             count+=1
        # return count
        # count = 0
        # j = 0
        # for i in range(n):
        #     while sum(islice(nums, j, i+1))>k:
        #         j+=1
        #     if sum(islice(nums, j, i+1))==k:
        #         count+=1
        # return count
        s = 0
        m = {}
        m[0] = 1
        for i in nums:
            s += i
            if s-k in m:
                count+=m[s-k]
            # m[s] = 1
            m[s] = m.get(s, 0) + 1
        return count