"""
Problem: Cheapest Flights Within K Stops
Platform: LeetCode
Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/
Approach: BFS / Modified Dijkstra with Stops
Time Complexity: O(E * K)
Space Complexity: O(V + E)
"""

from collections import deque

class Solution(object):

    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """

        graph = [[] for _ in range(n)]

        for u, v, wt in flights:
            graph[u].append((v, wt))

        q = deque()
        q.append((0, src, 0))   # stops, node, cost

        dist = [float('inf')] * n
        dist[src] = 0

        while q:

            stops, node, cost = q.popleft()

            if stops > k:
                continue

            for nbr, wt in graph[node]:

                new_cost = cost + wt

                if new_cost < dist[nbr]:
                    dist[nbr] = new_cost
                    q.append((stops + 1, nbr, new_cost))

        if dist[dst] == float('inf'):
            return -1

        return dist[dst]


# Build a directed weighted graph from flights.
# Queue stores stops taken, current node, and current cost.
# Explore routes only while stops are within k.
# If reaching a neighbor gives cheaper cost, update dist.
# Push updated state into queue for further exploration.
# If destination remains infinity, no valid route exists.