class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = [i for i in nums if i>0]
        b = [i for i in nums if i<0]
        res = []
        i = 0
        while i<len(a):
            res.append(a[i])
            res.append(b[i])
            i+=1
        return res