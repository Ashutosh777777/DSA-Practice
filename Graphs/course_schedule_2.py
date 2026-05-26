"""
Problem: Course Schedule II
Platform: LeetCode
Link: https://leetcode.com/problems/course-schedule-ii/
Approach: BFS / Kahn's Algorithm
Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""

from collections import deque

class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        n = numCourses
        p = prerequisites[:]

        g = [[] for _ in range(n)]
        id = [0] * n

        for c, pr in p:
            g[pr].append(c)
            id[c] += 1

        q = deque()

        for i in range(n):

            if id[i] == 0:
                q.append(i)

        ans = []

        while q:

            node = q.popleft()
            ans.append(node)

            for nbr in g[node]:

                id[nbr] -= 1

                if id[nbr] == 0:
                    q.append(nbr)

        if len(ans) != n:
            return []

        return ans


# Build graph where prerequisite points to the course.
# id[] stores number of prerequisites for each course.
# Start with courses having zero prerequisites.
# Remove completed courses and reduce dependency count of neighbors.
# If all courses are processed, return valid order.
# If not, cycle exists, so return empty list.