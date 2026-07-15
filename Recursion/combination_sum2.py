class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        cur = []

        def solve(i, rem):
            if rem == 0 :
                res.append(cur[:])
                return
            if rem<0 or i == len(candidates):
                return
            
            cur.append(candidates[i])
            solve(i+1, rem-candidates[i])
            cur.pop()

            while i +1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1 

            solve(i+1, rem)
        solve(0, target)
        return res