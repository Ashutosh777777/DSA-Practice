from collections import deque
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # a = [nums[0]]
        # b = deque([nums[-1]])
        n = len(nums)
        # for i in range(1, n):
        #     a.append(a[-1]*nums[i])
        #     b.appendleft(b[0]*nums[n-i-1])
        # return max(max(a), max(b), max(nums))
        p = 1
        s = 1
        m = -1*float('inf')
        for i in range(n):
            if p == 0:
                p = 1
            if s == 0:
                s = 1
            p = p*nums[i]
            s = s*nums[n-i-1]

            m = max(m, p, s)
        return m