class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7

        def power(x, y):
            if y == 0:
                return 1

            half = power(x, y // 2)

            if y % 2:
                return (half * half * x) % MOD
            return (half * half) % MOD

        even = (n + 1) // 2
        odd = n // 2

        return (power(5, even) * power(4, odd)) % MOD