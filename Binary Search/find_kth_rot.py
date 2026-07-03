class Solution:
    def findKRotation(self, arr):
        # code here
        if len(arr)==0 or len(arr)==1:
            return 0
        s = 0
        e = len(arr)-1
        if arr[s]<=arr[e]:
            return 0
        n = len(arr)
        while s<=e:
            m = (s+e)//2
            
            if arr[m]<=arr[(m+1)%n] and arr[m]<= arr[(m-1)%n]:
                res = m
                break
            elif arr[m]<=arr[e]:
                e = m-1
            else:
                s = m+1
        return res