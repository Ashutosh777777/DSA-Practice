from bisect import bisect_left

class Solution:
    def lis(self, arr):
        temp = []

        for x in arr:
            idx = bisect_left(temp, x)

            if idx == len(temp):
                temp.append(x)
            else:
                temp[idx] = x

        return len(temp)
    
    
# The Below code cause TLE even after memoization.

class Solution:
    def lis(self, arr):
        # # code here
        # s1 = arr[:]
        s2 = sorted(set(arr))
    
        m = len(arr)
        n = len(s2)
        t = [[0]*(n+1) for _ in range(m+1)]
        
        def solve(s1, s2):
            # m = len(s2)
        #     n = len(s1)
        #     if m == 0 or n == 0:
        #         return 0
            
        #     if s1[n-1]==s2[m-1]:
        #         return 1 + solve(s1[:n-1], s2[:m-1])
        #     else:
        #         return max(solve(s1[:n-1], s2[:]), solve(s1[:], s2[:m-1]))
        # return solve(arr, s2)
            if not s1 or not s2:
                return 0
            for i in range(1, m+1):
                for j in range(1, n+1):
                    
                    if s1[i-1]==s2[j-1]:
                        t[i][j] = 1 + t[i-1][j-1]
                    else:
                        t[i][j] = max(t[i-1][j], t[i][j-1])
            return t[m][n]
        return solve(arr, s2)