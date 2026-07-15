class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        cur = []

        def solve(i, rem):
            if rem == 0 :
                res.append(cur[:])
                return
            if rem<0 or i == len(candidates):
                return
            
            cur.append(candidates[i])
            solve(i, rem-candidates[i])
            cur.pop()
            solve(i+1, rem)
        solve(0, target)
        return res