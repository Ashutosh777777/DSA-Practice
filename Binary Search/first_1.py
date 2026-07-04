class Solution:
    def firstIndex(self, arr):
    # Your code goes here

        n = len(arr)
        if arr[-1] == 0:
            return -1
        s = 0
        e = n-1
        while s<=e:
            m = (s+e)//2
            
            if arr[m]==0:
                s = m+1
            else:
                if m == 0 or arr[m-1]==0:
                    return m
                e = m-1
        return -1