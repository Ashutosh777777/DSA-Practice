class Solution:
    def find(self, arr, x):
        # code here
        s = 0
        e = len(arr)-1
        target = -1
        while s<=e:
            m = (s+e)//2
            
            if arr[m]==x:
                target = m
                break
            elif arr[m]>x:
                e = m-1
            else:
                s = m+1
        if target == -1:
            return [-1, -1]
        p1 = target
        p2 = target
        
        while p1>=0 and arr[p1] == x:
            p1-=1
        while p2<len(arr) and arr[p2]==x :
            p2+=1
        return [p1+1, p2-1]