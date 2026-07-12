class Solution(object):
    def minimumCost(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m = 10**9 + 7

        a = k
        b = 0
        c = 0

        for d in nums:
            if a < d:
                e = (d - a + k - 1) // k
                f = b + e
                c += f * (f + 1) // 2 - b * (b + 1) // 2
                c %= m
                a += e * k
                b = f

            a -= d

        return c