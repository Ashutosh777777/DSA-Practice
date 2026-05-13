"""
Problem: Generate Parentheses
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/generate-all-possible-parentheses/1
Approach: Backtracking / Recursion
Time Complexity: O(2^n)
Space Complexity: O(n)
"""

class Solution:

    def generateParentheses(self, n):
        # code here

        res = []
        lim = n // 2

        # Brute Force Recursion
        # def solve(i, s):
        #
        #     if i == 0:
        #         if s not in res:
        #             res.append(s)
        #         return
        #
        #     if s.count('(') > lim or s.count(')') > lim:
        #         return
        #
        #     if s.count('(') < s.count(')'):
        #         return
        #
        #     solve(i - 1, s + "(")
        #     solve(i - 1, s + ")")
        #
        # solve(n, "")
        # return res

        # Optimized Backtracking
        def solve(s, o, c):

            if len(s) == n:
                res.append(s)
                return

            if o < lim:
                solve(s + "(", o + 1, c)

            if c < o:
                solve(s + ")", o, c + 1)

        solve("", 0, 0)

        return res


# Use backtracking to generate only valid parentheses strings.
# o and c represent number of opening and closing brackets used.
# Add '(' only if opening brackets are still available.
# Add ')' only if closing brackets are less than opening brackets.
# This avoids generating invalid combinations entirely.