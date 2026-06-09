"""
Problem: Bellman-Ford Algorithm
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1
Approach: Bellman-Ford (Edge Relaxation)
Time Complexity: O(V * E)
Space Complexity: O(V)
"""

class Solution:

    def bellmanFord(self, V, edges, src):

        dist = [10**8] * V
        dist[src] = 0

        # Relax all edges V-1 times
        for _ in range(V - 1):

            for edge in edges:

                node = edge[0]
                nbr = edge[1]
                wt = edge[2]

                if dist[node] == 10**8:
                    continue

                new_dist = dist[node] + wt

                if new_dist < dist[nbr]:
                    dist[nbr] = new_dist

        # Check for negative weight cycle
        for edge in edges:

            node = edge[0]
            nbr = edge[1]
            wt = edge[2]

            if dist[node] == 10**8:
                continue

            new_dist = dist[node] + wt

            if new_dist < dist[nbr]:
                return [-1]

        return dist


# Initialize all distances as infinity except source.
# Relax every edge exactly V-1 times.
# Relaxation means updating distance if a shorter path is found.
# After V-1 iterations, shortest paths are finalized.
# Perform one extra pass to detect negative weight cycles.
# If any edge can still be relaxed, a negative cycle exists.