"""
Problem: Assign Cookies
Platform: LeetCode
Link: https://leetcode.com/problems/assign-cookies/
Approach: Greedy (two pointers after sorting)
Time Complexity: O(n log n + m log m) due to sorting
Space Complexity: O(1) (ignoring input modification) / O(n) if using deque
"""
from collections import deque
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        g = deque(g)
        s = deque(s)
        count = 0
        while s and g:
            if s[0]>=g[0]:
                g.popleft()
                
                count+=1
            s.popleft()
        return count
    
# Sort both children’s greed factors and cookie sizes in ascending order.
# Use two pointers (or queues) to try satisfying the least greedy child first.
# If the current cookie can satisfy the child, assign it and move both pointers.
# Otherwise, discard the cookie and try the next larger one.