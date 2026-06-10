"""
Problem: Floyd Warshall Algorithm
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1
Approach: Dynamic Programming / All-Pairs Shortest Path
Time Complexity: O(V^3)
Space Complexity: O(1)
"""

# User function template for Python

class Solution:

    def floydWarshall(self, dist):
        # Code here

        n = len(dist)

        for k in range(n):

            for i in range(n):

                for j in range(n):

                    if (
                        dist[i][k] != 10**8 and
                        dist[k][j] != 10**8
                    ):
                        dist[i][j] = min(
                            dist[i][j],
                            dist[i][k] + dist[k][j]
                        )


# Floyd-Warshall finds shortest paths between every pair of vertices.
# k represents the intermediate vertex allowed in the path.
# Check if path i → k → j is shorter than current i → j path.
# Update distance matrix whenever a shorter path is found.
# After all iterations, dist[i][j] stores the shortest distance
# between every pair of vertices.