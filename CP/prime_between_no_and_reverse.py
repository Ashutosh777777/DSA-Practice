"""
Problem: Sum of Primes Between Number and Its Reverse
Platform: LeetCode Weekly Contest 500
Link: https://leetcode.com/contest/weekly-contest-500/problems/sum-of-primes-between-number-and-its-reverse/
Approach: Reverse Number + Prime Check in Range
Time Complexity: O(range * sqrt(n))
Space Complexity: O(1)
"""

class Solution(object):
    def sumOfPrimesInRange(self, n):
        def check(x):
            if x <= 1:
                return False

            i = 2
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 1

            return True

        r = int(str(n)[::-1])

        s = min(n, r)
        e = max(n, r)

        ans = 0
        for i in range(s, e + 1):
            if check(i):
                ans += i

        return ans

# Reverse the number using string slicing.
# Find range from min(n, reverse) to max(n, reverse).
# Check every number in this range for prime.
# Add all prime numbers and return their sum.