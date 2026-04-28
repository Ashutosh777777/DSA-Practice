class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        def solve(s1, s2):
            if s1==s2:
                return True
            if len(s1) <= 1:
                return False
            n = len(s1)
            flag = False
            for i in range(1, n):
                if (solve(s1[:i], s2[n-i:])==True and solve(s1[i:], s2[:n-i])==True) or (solve(s1[:i], s2[:i])==True and solve(s1[i:], s2[i:])==True):
                    flag = True
                    break
            return flag
        return solve(s1, s2)
    
# Must be memoized to avoid TLE due to overlapping subproblems.