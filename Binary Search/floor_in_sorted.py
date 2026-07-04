class Solution:
    def findFloor(self, arr, x):
        # code here
        s = 0
        n = len(arr)
        e = n-1
        
        if x < arr[0]:
            return -1
        if x >= arr[-1]:
            return len(arr) - 1

        while s <= e:
            m = (s + e) // 2

            if arr[m] <= x and (m == len(arr)-1 or arr[m+1] > x):
                return m

            elif arr[m] > x:
                e = m - 1
            else:
                s = m + 1

        return -1