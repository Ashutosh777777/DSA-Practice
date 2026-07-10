class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def possible(m):
            sub = 1
            S = 0
            for x in nums:
                if S+x<=m:
                    S+=x
                else:
                    sub+=1
                    S = x
                    if sub>k:
                        return False
            return True
        
        s = max(nums)
        e = sum(nums)
        ans = -1

        while s<=e:
            mid = s + (e-s)//2
            if possible(mid):
                ans = mid
                e = mid-1
            else:
                s = mid+1
        return ans

