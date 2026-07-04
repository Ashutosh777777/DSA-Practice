class Solution:
    def findCeil(self, arr, x):
        # code here
        s = 0
        n = len(arr)
        e = n-1
        
        ans = -1
        while s<=e:
            m = (s+e)//2
            
            if arr[m]>=x:
                ans = m
                e = m-1
            else:
                s = m + 1
        return ans