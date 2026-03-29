"""
Problem: kth symbol in grammar
Platform: LeetCode
Link: https://leetcode.com/problems/k-th-symbol-in-grammar/
Approach: Recursion and bit manipulation
Time Complexity: O(n)
"""



class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n==1:
            return 0
        parent = self.kthGrammar(n-1, (k+1)//2)
        if k%2==1:
            return parent
        else:
            return 1 - parent
        
        
        
        
# Don’t build the string — use recursion (parent-child relation).
# Parent index = (k + 1) // 2 in row n-1.
# If k is odd → same as parent; if even → flipped (1 - parent).
# Base case: n == 1 → return 0.