"""
Problem: Number of Islands
Platform: LeetCode
Link: https://leetcode.com/problems/number-of-islands/
Approach: DFS / Grid Traversal
Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""

class Solution(object):

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        r = len(grid)
        c = len(grid[0])

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        def dfs(i, j):

            if (
                i < 0 or
                j < 0 or
                i >= r or
                j >= c or
                grid[i][j] != "1"
            ):
                return

            grid[i][j] = "2"

            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]

                dfs(ni, nj)

        count = 0

        for i in range(r):

            for j in range(c):

                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1

        return count


# Traverse every cell in the grid.
# Whenever an unvisited land cell "1" is found, start DFS.
# DFS marks the entire connected island as visited using "2".
# Explore 4 directions: up, right, down, and left.
# Each DFS call represents one complete island.
# Count how many times DFS is started.