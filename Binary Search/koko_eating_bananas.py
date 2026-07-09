import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        s = 1
        e = max(piles)
        def possible(m):
            hours = 0
            for pile in piles:
                hours+=math.ceil(pile / float(m))
            return hours<=h
        while s<=e:
            m = (s+e)//2
            if possible(m):
                e = m-1
            else:
                s = m+1
        return s