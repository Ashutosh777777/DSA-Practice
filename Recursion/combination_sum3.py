class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        cur = []

        def solve(i, rem):
            if rem == 0 and len(cur) == k:
                res.append(cur[:])
                return

            if rem < 0 or i > 9 or len(cur) > k:
                return

            cur.append(i)
            solve(i + 1, rem - i)
            cur.pop()

            solve(i + 1, rem)

        solve(1, n)
        return res