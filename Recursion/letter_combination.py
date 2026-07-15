class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        d2c = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz",}

        def solve(i, cur):
            if len(cur) == len(digits):
                res.append(cur)
                return
            for c in d2c[digits[i]]:
                solve(i+1, cur+c)
        if digits:
            solve(0, "")
        return res