"""
Problem: Minimum Jumps
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1
Approach: Greedy / BFS Level Traversal
Time Complexity: O(n)
Space Complexity: O(1)
"""

# User function Template for python3

class Solution:

    def minJumps(self, arr):
        # code here

        n = len(arr)

        if n <= 1:
            return 0

        if arr[0] == 0:
            return -1

        l = 0
        r = 0
        res = 0

        while r < len(arr) - 1:

            maxi = 0

            for i in range(l, r + 1):
                maxi = max(maxi, i + arr[i])

            if maxi == r:
                return -1

            l = r + 1
            r = maxi

            res += 1

        return res


# Treat each jump range as one BFS level.
# [l, r] represents all indices reachable in current jump.
# Find the farthest index reachable from current range.
# Move to next level using new boundaries.
# If range cannot expand further → destination is unreachable.