import heapq
class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # code here
        adj = [[] for _ in range(V)]

        for u, v, wt in edges:
            adj[u].append((v, wt))
            adj[v].append((u, wt))
        dist = [float("inf")] * V
        dist[src] = 0

        pq = [(0, src)]

        while pq:
            d, node = heapq.heappop(pq)

            if d > dist[node]:
                continue

            for nbr, wt in adj[node]:
                nd = d + wt

                if nd < dist[nbr]:
                    dist[nbr] = nd
                    heapq.heappush(pq, (nd, nbr))

        for i in range(V):
            if dist[i] == float("inf"):
                dist[i] = -1

        return dist