from itertools import islice
class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """

        if m * k > len(bloomDay):
            return -1
        n = len(bloomDay)
        def possible(mid):
            # count = 0
            # for i in range(n-k):
            #     if max(islice(bloomDay, i, i+k))<=mid:
            #         count+=1
            # return m<=count
            f = 0
            b = 0
            for day in bloomDay:
                if day<=mid:
                    f+=1
                    if f==k:
                        b+=1
                        f = 0
                else:
                    f = 0
            return b>=m
        s = min(bloomDay)
        e = max(bloomDay)
        while s<=e:
            mid = (s+e)//2
            if possible(mid):
                e = mid-1
            else:
                s = mid+1
        return s