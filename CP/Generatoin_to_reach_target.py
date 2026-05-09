"""
Problem: Minimum Generations to Reach Target
Platform: LeetCode
Link: 
Approach: Set Simulation / Pairwise Average Generation
Time Complexity: O(g * p^2)
Space Complexity: O(p)
"""

class Solution(object):
    def minGenerations(self, points, target):
        """
        :type points: List[List[int]]
        :type target: List[int]
        :rtype: int
        """

        p = set(tuple(x) for x in points)
        t = tuple(target)

        if t in p:
            return 0

        mn = [min(x[i] for x in p) for i in range(3)]
        mx = [max(x[i] for x in p) for i in range(3)]

        for i in range(3):
            if t[i] < mn[i] or t[i] > mx[i]:
                return -1

        g = 0

        while True:
            g += 1
            arr = list(p)
            new = set()

            for i in range(len(arr)):
                for j in range(i + 1, len(arr)):
                    a = arr[i]
                    b = arr[j]

                    c = (
                        (a[0] + b[0]) // 2,
                        (a[1] + b[1]) // 2,
                        (a[2] + b[2]) // 2
                    )

                    if c == t:
                        return g

                    if c not in p:
                        new.add(c)

            if not new:
                return -1

            p.update(new)


# Store all available points in a set for fast lookup.
# If target already exists → 0 generations needed.
# If target lies outside min/max coordinate range → impossible.
# In each generation, create new points by averaging every pair.
# If target is generated → return current generation count.
# If no new points are created → target can never be reached.