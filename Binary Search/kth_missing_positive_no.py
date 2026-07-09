class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        s = 0
        e = len(arr)-1
        m = -1
        while s<=e:
            m = s + (e-s)//2
            missing = arr[m]-(m+1)

            if missing<k:
                s = m+1
            else:
                e = m-1
        return s+k